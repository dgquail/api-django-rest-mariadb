from django.db import models

class Speech(models.Model):
    speaker = models.ForeignKey(
        'Speaker', 
        on_delete=models.CASCADE, 
        related_name='speeches', 
        help_text="The speaker who delivered the speech."
    )
    language = models.ForeignKey(
        'Language', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='speeches', 
        help_text="The language in which the speech was delivered."
    )
    source = models.ForeignKey(
        'Source', 
        on_delete=models.SET_NULL, 
        null=True, 
        related_name='speeches', 
        help_text="The source of the speech, e.g., Twitter, a blog, or a media outlet."
    )
    date = models.DateField(
        help_text="The date when the speech was delivered."
    )
    content = models.TextField(
        help_text="The text content of the speech."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="The date and time when the speech record was created."
    )
    updated_at = models.DateTimeField(
        auto_now=True, 
        help_text="The date and time when the speech record was last updated."
    )

    class Meta:
        verbose_name = "Speech"
        verbose_name_plural = "Speeches"
        ordering = ['-date', 'speaker']

    def __str__(self):
        return f"Speech by {self.speaker} on {self.date}"
