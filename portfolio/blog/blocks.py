from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    TextBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageBlock

class CaptionedImageBlock(StructBlock):
    image = ImageBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "blog/captioned_image_block.html"
# a small struct to allow using of code blocks in the blog.
# These are the languages that are available for the ditor to pick from the code block.
LANG_CHOICES = [
    ("python", "Python"),
    ("javascript", "JavaScript"),
    ("html", "HTML"),
    ("css", "CSS"),
    ("bash", "Bash"),
    ("json", "JSON"),
    ("plaintext", "Plain text"),
]
class CodeBlock(StructBlock):
    language = ChoiceBlock(choices=LANG_CHOICES, default="plaintext")
    code     = TextBlock(rows=12)

    class Meta:
        icon = "code"
        label = "Code"
        template = "blog/code_block.html"

class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "blog/heading_block.html"

class BaseStreamBlock(StreamBlock):
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(icon="pilcrow", features=["bold","italic","link","code","ol","ul", "h1", "blockquote"])
    image_block = CaptionedImageBlock()
    embed_block = EmbedBlock(
        help_text="Insert a URL to embed.", icon="media",
    )
    code_block      = CodeBlock()