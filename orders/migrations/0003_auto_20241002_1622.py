# Generated by Django 3.1 on 2024-10-02 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_pincode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='pincode',
            field=models.CharField(default='000000', max_length=10),
        ),
    ]