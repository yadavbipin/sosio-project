# Generated by Django 2.1.2 on 2018-10-18 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyExpense', '0003_auto_20181018_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
