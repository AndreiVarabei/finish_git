# Generated by Django 4.0.3 on 2022-03-31 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0014_goodcompanies_delete_tikers_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companies',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='goodcompanies',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
