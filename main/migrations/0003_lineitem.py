# Generated by Django 4.2.1 on 2023-05-29 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_manufacturer_site_note_part'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('note', models.TextField(blank=True, default='')),
                ('item_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.part')),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.workorder')),
            ],
            options={
                'verbose_name': 'Line Item',
                'verbose_name_plural': 'Line Items',
                'ordering': ('part', '-pk'),
            },
        ),
    ]
