# Generated by Django 3.1 on 2024-10-02 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pincode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]