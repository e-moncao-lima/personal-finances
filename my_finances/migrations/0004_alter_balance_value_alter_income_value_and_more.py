# Generated by Django 4.1.7 on 2023-03-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_finances', '0003_balance_updated_at_alter_balance_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='income',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
