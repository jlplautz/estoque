# Generated by Django 3.0.6 on 2020-05-18 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20191005_0359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='ncm',
            field=models.CharField(max_length=13, verbose_name='NCM'),
        ),
    ]

