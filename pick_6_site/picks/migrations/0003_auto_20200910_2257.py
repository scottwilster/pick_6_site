# Generated by Django 3.1.1 on 2020-09-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0002_auto_20200910_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pick',
            name='pub_date',
            field=models.DateTimeField(default=True, verbose_name='date published'),
        ),
    ]
