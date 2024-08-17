# Generated by Django 5.1 on 2024-08-17 17:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('photographer', '0002_alter_photographer_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('scheduled_on', models.DateTimeField()),
                ('modified', models.DateTimeField(auto_now=True)),
                ('interview_type', models.CharField(choices=[('In person', 'In person'), ('Virtual', 'Virtual')], default='In Person', max_length=35)),
                ('scheduled_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer', verbose_name='Client')),
                ('scheduled_with', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photographer.photographer', verbose_name='Photographer')),
            ],
            options={
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photoshoot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('scheduled_on', models.DateTimeField()),
                ('modified', models.DateTimeField(auto_now=True)),
                ('venue', models.CharField(help_text='Location of the photoshoot venue', max_length=255, null=True)),
                ('scheduled_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.customer', verbose_name='Client')),
                ('scheduled_with', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='photographer.photographer', verbose_name='Photographer')),
            ],
            options={
                'ordering': ['created_on'],
                'abstract': False,
            },
        ),
    ]
