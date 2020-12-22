======================
 Wagtail Image Upload
======================

We need users to upload images, but do not want them to see everyone
else's images, which the Wagtail Image does -- from the "root"
collection. But we also like the ability to see the uploaded images,
which the Django ImageField does not do.

So we want a UX that lets us group images for a parent model, re-order
them, but see the graphics instead of showing the disk path.

Turns out not to be that hard, if we subclass the Django widget and
add an "img" tag.

Downside is that we don't get Wagtail's handy auto-resized renditions,
so our performance won't be as nice.
