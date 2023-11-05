# Generated by Django 4.2.4 on 2023-10-07 21:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0008_items_views_feedbacks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbacks',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
