# Generated by Django 4.0.3 on 2022-04-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_remove_waitinguser_type_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='link',
            field=models.ImageField(blank=True, null=True, upload_to='image_profils'),
        ),
    ]
