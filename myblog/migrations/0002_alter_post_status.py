# Generated by Django 3.2.6 on 2021-09-18 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('published', 'PUBLISHED'), ('draft', 'DRAFT')], max_length=50),
        ),
    ]