# Generated by Django 5.1.4 on 2024-12-29 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_coments_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='coments',
            name='signature',
            field=models.CharField(default='Firma', max_length=100),
        ),
    ]