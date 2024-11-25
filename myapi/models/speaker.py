from django.db import models

class Speaker(models.Model):
    first_name = models.CharField(max_length=50, help_text="Speaker's first name.")
    last_name = models.CharField(max_length=50, help_text="Speaker's last name.")
    email = models.EmailField(unique=True, help_text="Speaker's unique email address.")
    social_x_account = models.CharField(
        max_length=100, 
        unique=True, 
        help_text="The username or account name on social network X."
    )
    social_x_id = models.CharField(
        max_length=50, 
        unique=True, 
        help_text="The unique ID of the speaker on social network X."
    )
    bio = models.TextField(blank=True, null=True, help_text="Short biography or description of the speaker.")
    language = models.ForeignKey(
        'Language', 
        on_delete=models.SET_NULL, 
        null=True, 
        help_text="Primary language of the speaker."
    )
    is_active = models.BooleanField(default=True, help_text="Indicates whether the speaker's account is active.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the speaker profile was created.")
    updated_at = models.DateTimeField(auto_now=True, help_text="The date and time when the speaker profile was last updated.")

    class Meta:
        verbose_name = "Speaker"
        verbose_name_plural = "Speakers"
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.social_x_account})"
