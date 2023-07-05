# Generated by Django 4.2.2 on 2023-07-05 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_remove_order_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='orders', through='demo.OrderPosition', to='demo.product'),
        ),
    ]