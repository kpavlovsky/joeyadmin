# Generated by Django 4.2.1 on 2023-05-29 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_part_link_part_part_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineitem',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='extended_cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='location',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='source',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
