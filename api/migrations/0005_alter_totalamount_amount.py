# Generated by Django 3.2.4 on 2021-11-03 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_totalamount_user_linked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalamount',
            name='amount',
            field=models.FloatField(),
        ),
    ]
