# Generated by Django 4.0.5 on 2022-06-12 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_remove_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='rate',
            name='rate',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
