# Generated by Django 3.1.3 on 2021-01-18 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_booksale_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='booksale',
            name='author',
            field=models.CharField(default=100, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booksale',
            name='date',
            field=models.DateField(auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booksale',
            name='genre',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
