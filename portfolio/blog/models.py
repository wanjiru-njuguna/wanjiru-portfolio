from django.db import models
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.html import strip_tags
from django.utils.text import Truncator
from django.utils import timezone
from django.shortcuts import render, redirect

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.snippets.models import register_snippet
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
# importing the block for the richtextfield
from .blocks import BaseStreamBlock
# from .forms import CommentForm

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = BlogPage.objects.child_of(self).live().order_by('-first_published_at')
        paginator = Paginator(blogpages, 5)
        page = request.GET.get("page")
        try:
            blogpages = paginator.page(page)
        except PageNotAnInteger:
            blogpages = paginator.page(1)
        except EmptyPage:
            blogpages = paginator.page(paginator.num_pages)

        context['blogpages'] = blogpages
        return context

class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogPage(Page):
    date = models.DateField("post date")
    # intro = models.CharField(max_length=250, blank=True)
    summary = models.CharField(max_length=300, blank=True)
    body = StreamField(BaseStreamBlock(), use_json_field=True, blank=True,default=list,)
    authors = ParentalManyToManyField('blog.Author', blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            "date",
            FieldPanel("authors", widget=forms.CheckboxSelectMultiple),"tags",
        ], heading="Blog information"),
        "body", "gallery_images",
    ]
    def get_excerpt(self, words=40):
         texts = []
         if not self.body:
            return ""
         for block in self.body:
            
            if block.block_type in ("paragraph_block", "heading_block"):
                val = block.value
                html = str(val)  
                texts.append(strip_tags(html))
            # stop once we have enough text
            if len(" ".join(texts).split()) >= words * 2:
                break

         plain = " ".join(texts).strip()
         return Truncator(plain).words(words, truncate="…")
    def serve(self, request):
        
        from .forms import CommentForm

        context = super().get_context(request)
        comments = self.comments.filter(approved=True).order_by("-created_at")

        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                new_comment = form.save(commit=False)
                new_comment.post = self
                new_comment.save()
                return redirect(self.url + "#comments")
        else:
            form = CommentForm()

        context = self.get_context(request)
        context.update({"form": form, "comments": comments})
        return render(request, self.get_template(request), context)

class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = ["image", "caption"]

# model for the authors of the blog. It is registered as a snippet since the author model isn't a pag perse.
@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = ["name", "author_image"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Authors'

# model to fileter the blog posts using tags.
class BlogTagIndexPage(Page):

    def get_context(self, request):

        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context
    

# model for the blogs' comments.
class Comment (models.Model):
    post = models.ForeignKey(
        "BlogPage",
        on_delete=models.CASCADE,
        related_name="comments",
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    website = models.URLField(blank=True)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)
    def __str__(self):
        return f"Comment by {self.name} on {self.post}"
