# Generated by Django 5.1.1 on 2024-10-05 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_remove_orderproduct_color_remove_orderproduct_size'),
        ('store', '0005_alter_product_id_alter_variation_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
