# Generated by Django 3.1.2 on 2020-11-24 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Produkty', '0002_auto_20201124_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkty',
            name='producent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Produkty.producent'),
        ),
    ]