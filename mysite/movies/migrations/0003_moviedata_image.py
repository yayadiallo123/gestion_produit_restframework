# Generated by Django 5.0.1 on 2024-01-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_moviedata_typ"),
    ]

    operations = [
        migrations.AddField(
            model_name="moviedata",
            name="image",
            field=models.ImageField(default="Images/d.jpg", upload_to="Images"),
        ),
    ]
