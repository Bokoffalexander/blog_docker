# Generated by Django 5.0.7 on 2024-07-22 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='owner',
        ),
    ]
