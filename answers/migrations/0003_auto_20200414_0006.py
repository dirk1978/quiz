# Generated by Django 3.0.5 on 2020-04-13 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_auto_20200413_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='submitted',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
