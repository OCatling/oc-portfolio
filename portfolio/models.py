from django.db import models


class Project(models.Model):
    """Model For Standard Portfolio Piece"""

    # Descriptive
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='portfolio/media', blank=True)

    # Functional
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField
    isLive = models.BooleanField(default=False)

    # Dates & Time
    publication_date = models.DateField(auto_now=True)
    creation_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """Return Objects Url"""

        from django.core.urlresolvers import reverse
        return reverse('project-detail', kwargs={"slug": self.slug, })

    def __str__(self):
        """Get String Value OF Class"""
        return self.title