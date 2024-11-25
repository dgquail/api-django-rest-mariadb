# Generated by Django 5.1.3 on 2024-11-25 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_user', models.CharField(help_text="Username for the platform's X account.", max_length=100)),
                ('x_user_id', models.CharField(help_text="Unique identifier for the platform's X account.", max_length=50, unique=True)),
                ('x_password', models.CharField(help_text="Password for the platform's X account.", max_length=128)),
                ('email', models.EmailField(help_text='Email address for platform notifications or recovery.', max_length=254)),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text="Language code, e.g., 'en' for English.", max_length=10, unique=True)),
                ('name', models.CharField(help_text="Full name of the language, e.g., 'English'.", max_length=100)),
                ('is_active', models.BooleanField(default=True, help_text='Indicates whether the language is active or not.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the language was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time when the language was last updated.')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the source, e.g., Twitter, a blog, or a print media.', max_length=100, unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional description of the source.', null=True)),
                ('url', models.URLField(blank=True, help_text='URL of the source, if applicable (e.g., a blog or social media profile).', null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Indicates whether the source is active or can be used.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the source was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time when the source was last updated.')),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="Speaker's first name.", max_length=50)),
                ('last_name', models.CharField(help_text="Speaker's last name.", max_length=50)),
                ('email', models.EmailField(help_text="Speaker's unique email address.", max_length=254, unique=True)),
                ('social_x_account', models.CharField(help_text='The username or account name on social network X.', max_length=100, unique=True)),
                ('social_x_id', models.CharField(help_text='The unique ID of the speaker on social network X.', max_length=50, unique=True)),
                ('bio', models.TextField(blank=True, help_text='Short biography or description of the speaker.', null=True)),
                ('is_active', models.BooleanField(default=True, help_text="Indicates whether the speaker's account is active.")),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the speaker profile was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time when the speaker profile was last updated.')),
                ('language', models.ForeignKey(help_text='Primary language of the speaker.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapi.language')),
            ],
            options={
                'verbose_name': 'Speaker',
                'verbose_name_plural': 'Speakers',
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(help_text='The date when the speech was delivered.')),
                ('content', models.TextField(help_text='The text content of the speech.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the speech record was created.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time when the speech record was last updated.')),
                ('language', models.ForeignKey(help_text='The language in which the speech was delivered.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='speeches', to='myapi.language')),
                ('source', models.ForeignKey(help_text='The source of the speech, e.g., Twitter, a blog, or a media outlet.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='speeches', to='myapi.source')),
                ('speaker', models.ForeignKey(help_text='The speaker who delivered the speech.', on_delete=django.db.models.deletion.CASCADE, related_name='speeches', to='myapi.speaker')),
            ],
            options={
                'verbose_name': 'Speech',
                'verbose_name_plural': 'Speeches',
                'ordering': ['-date', 'speaker'],
            },
        ),
    ]
