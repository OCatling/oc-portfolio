from django.db import models
from django.urls import reverse


class Project(models.Model):
    """Model For Standard Portfolio Piece"""

    # Descriptive
    title = models.CharField(max_length=250)
    tagline = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(blank=True)

    # Functional
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    isLive = models.BooleanField(default=False)

    # Dates & Time
    publication_date = models.DateField(auto_now=True)
    creation_date = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        """Return Objects Url"""
        return reverse('portfolio:work', kwargs={"slug": self.slug, })

    def snippet(self):
        return self.description[:50] + '....'

    def __str__(self):
        """Get String Value OF Class"""
        return self.title


class Page(models.Model):
    """Model For Pages"""

    # Descriptive
    title = models.CharField(max_length=250)
    tagline = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)

    # Functional
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    isLive = models.BooleanField(default=False)
    isInvert = models.BooleanField(default=False)
    isTitleVisable = models.BooleanField(default=False)

    # Dates & Time
    publication_date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        """Return Objects Url"""
        return reverse('portfolio:work', kwargs={"slug": self.slug, })

    def __str__(self):
        """Get String Value OF Class"""
        return self.title
