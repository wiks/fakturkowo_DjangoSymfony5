# Generated by Django 3.0.5 on 2020-04-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoicesitems',
            name='items_number',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
