# Generated by Django 2.2.17 on 2021-03-23 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upskill_photography', '0006_auto_20210323_1109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=5, default=None, max_digits=8, null=True),
        ),
    ]