# Generated by Django 4.1.4 on 2022-12-21 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_short_description'),
        ('orders', '0013_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinbasket',
            name='product',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product'),
        ),
    ]
