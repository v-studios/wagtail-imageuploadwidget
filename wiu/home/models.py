from django.db import models
from django.forms import widgets

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel("body"),
        InlinePanel("property_photo", label="Photos", min_num=0, max_num=9),
        InlinePanel("photo1", label="Photo1", min_num=0, max_num=9),
    ]


class PropertyPhoto(Orderable):
    page = ParentalKey(
        HomePage, on_delete=models.CASCADE, related_name="property_photo"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(max_length=32, blank=True, null=True)
    panels = [
        ImageChooserPanel("image"),
        FieldPanel("caption"),
    ]


class ClearableImageInput(widgets.ClearableFileInput):
    """Show a thumbnail of the image in the Image Input form."""

    template_name = "clearable_image_input.html"


class Photo1(Orderable):
    # WagTail puts in media/original_images/, and media/images/
    # Django makes upload names unique by suffixing second such name.
    # We do not have access here to self to get self.page_id for association.
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="photo1")
    image = models.ImageField(blank=False, null=False, upload_to="property/photos/")
    caption = models.CharField(max_length=32, blank=True, null=True)

    panels = [
        FieldPanel("image", widget=ClearableImageInput),
        FieldPanel("caption"),
    ]
