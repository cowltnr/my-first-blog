# Generated by Django 4.1 on 2023-05-16 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]