# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('name', models.TextField()),
                ('lifeform', models.BooleanField(default=False)),
                ('perish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_id', models.IntegerField()),
                ('system_name', models.TextField()),
                ('cbody_id', models.IntegerField(null=True)),
                ('cbody_name', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MarketEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy_or_sell', models.IntegerField(choices=[(1, 'Buy'), (2, 'Sell')])),
                ('quant', models.IntegerField()),
                ('price', models.FloatField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Starbase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starbase_id', models.IntegerField()),
                ('aff', models.TextField(max_length=3)),
                ('name', models.TextField()),
                ('hiport', models.BooleanField()),
                ('patch_price', models.IntegerField()),
                ('dock_capacity', models.IntegerField()),
                ('maint_complexes', models.IntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Location')),
            ],
        ),
        migrations.AddField(
            model_name='marketentry',
            name='starbase_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Starbase'),
        ),
    ]
