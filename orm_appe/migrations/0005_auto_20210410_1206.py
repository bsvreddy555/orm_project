# Generated by Django 2.1 on 2021-04-10 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orm_appe', '0004_auto_20210405_2014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='ph',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orm_appe.STUDENT'),
        ),
    ]