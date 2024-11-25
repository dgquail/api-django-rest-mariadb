from django.db import models

class Config(models.Model):
    x_user = models.CharField(
        max_length=100, 
        help_text="Username for the platform's X account."
    )
    x_user_id = models.CharField(
        max_length=50, 
        unique=True, 
        help_text="Unique identifier for the platform's X account."
    )
    x_password = models.CharField(
        max_length=128, 
        help_text="Password for the platform's X account."
    )
    email = models.EmailField(
        help_text="Email address for platform notifications or recovery."
    )

    class Meta:
        verbose_name = "Configuration"
        verbose_name_plural = "Configurations"

    def __str__(self):
        return f"Configuration for X User: {self.x_user}"
