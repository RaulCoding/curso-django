# Generated by Django 5.1.4 on 2024-12-29 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coments',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
