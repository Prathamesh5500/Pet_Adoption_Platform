# Generated by Django 5.0.4 on 2024-06-06 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('sellername', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('adoptionfee', models.IntegerField(default=0)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Details',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('gender', models.CharField(default='male', max_length=10)),
                ('size', models.CharField(default='small', max_length=10)),
                ('color', models.CharField(default='black', max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('spayed', models.CharField(default='no', max_length=10)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoption.seller')),
            ],
        ),
    ]
