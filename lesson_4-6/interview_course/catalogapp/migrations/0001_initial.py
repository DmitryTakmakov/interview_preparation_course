# Generated by Django 3.2.9 on 2021-11-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=128, verbose_name='product name')),
                ('added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='price')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='product quantity')),
                ('supplier_name', models.CharField(max_length=128, verbose_name='supplier name')),
            ],
        ),
    ]
