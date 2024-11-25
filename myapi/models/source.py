from django.db import models

class Source(models.Model):
    name = models.CharField(
        max_length=100, 
        unique=True, 
        help_text="Name of the source, e.g., Twitter, a blog, or a print media."
    )
    description = models.TextField(
        blank=True, 
        null=True, 
        help_text="Optional description of the source."
    )
    url = models.URLField(
        blank=True, 
        null=True, 
        help_text="URL of the source, if applicable (e.g., a blog or social media profile)."
    )
    is_active = models.BooleanField(
        default=True, 
        help_text="Indicates whether the source is active or can be used."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time when the source was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="The date and time when the source was last updated."
    )

    class Meta:
        verbose_name = "Source"
        verbose_name_plural = "Sources"
        ordering = ['name']

    def __str__(self):
        return self.name
