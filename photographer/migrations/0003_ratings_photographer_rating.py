# Generated by Django 5.1 on 2024-09-17 17:33

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0002_alter_photographer_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
            ],
        ),
        migrations.AddField(
            model_name='photographer',
            name='rating',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photographer.ratings'),
        ),
    ]
