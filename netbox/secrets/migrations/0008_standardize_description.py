# Generated by Django 3.0.3 on 2020-03-13 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0007_secretrole_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secretrole',
            name='description',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
