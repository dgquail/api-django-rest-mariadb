from django.db import models

class Language(models.Model):
    code = models.CharField(max_length=10, unique=True, help_text="Language code, e.g., 'en' for English.")
    name = models.CharField(max_length=100, help_text="Full name of the language, e.g., 'English'.")
    is_active = models.BooleanField(default=True, help_text="Indicates whether the language is active or not.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the language was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time when the language was last updated.")

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.code})"
