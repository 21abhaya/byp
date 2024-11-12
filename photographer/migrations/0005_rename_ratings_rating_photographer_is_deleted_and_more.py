# Generated by Django 5.1 on 2024-11-10 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photographer', '0004_alter_photographer_rate_review'),
    ]

    operations = [
    #     migrations.RenameModel(
    #         old_name='Ratings',
    #         new_name='Rating',
    #     ),
        # migrations.AddField(
        #     model_name='photographer',
        #     name='is_deleted',
        #     field=models.BooleanField(default=False),
        # ),
        migrations.AlterField(
            model_name='photographer',
            name='portfolio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photographer.portfolio'),
        ),
        migrations.RemoveField(
            model_name='photographer',
            name='rating',
        ),
        migrations.AddField(
            model_name='photographer',
            name='rating',
            field=models.ManyToManyField(null=True, to='photographer.ratings'),
        ),
    ]