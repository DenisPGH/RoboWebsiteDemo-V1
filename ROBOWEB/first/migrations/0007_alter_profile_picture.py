# Generated by Django 4.0.3 on 2022-04-15 13:39

import ROBOWEB.first.validatros
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_alter_images_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='image_profils', validators=[ROBOWEB.first.validatros.MaxFileSizeInMbValidator]),
        ),
    ]