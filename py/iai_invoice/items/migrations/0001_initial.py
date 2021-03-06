# Generated by Django 3.0.5 on 2020-04-25 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, default=None, null=True)),
                ('price_netto', models.DecimalField(decimal_places=2, max_digits=6)),
                ('jm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Jms')),
                ('vat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Vats')),
            ],
        ),
    ]
