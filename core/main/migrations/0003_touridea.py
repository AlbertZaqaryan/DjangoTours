# Generated by Django 4.0.5 on 2022-06-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_homebg_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourIdea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='TourIdea name')),
                ('about', models.TextField(verbose_name='TourIdea')),
                ('img', models.ImageField(upload_to='media', verbose_name='TourIdea image')),
            ],
            options={
                'verbose_name': 'TourIdea',
                'verbose_name_plural': 'TourIdeas',
            },
        ),
    ]
