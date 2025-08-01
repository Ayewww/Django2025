# Generated by Django 5.2.4 on 2025-07-31 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("created_date", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_date", models.DateTimeField(auto_now=True, null=True)),
                ("uploaded_image", models.ImageField(blank=True, upload_to="images/")),
                ("uploaded_file", models.FileField(blank=True, upload_to="files/")),
            ],
        ),
    ]
