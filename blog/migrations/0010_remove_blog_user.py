# Generated by Django 5.0.7 on 2024-07-23 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_blog_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
    ]
