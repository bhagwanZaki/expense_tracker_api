# Generated by Django 3.2.4 on 2021-10-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='incomeOrexpense',
            field=models.CharField(choices=[('income', 'Income'), ('expense', 'Expense'), ('saving', 'Saving')], max_length=7),
        ),
    ]
