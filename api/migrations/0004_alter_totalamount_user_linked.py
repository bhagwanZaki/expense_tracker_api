# Generated by Django 3.2.4 on 2021-11-03 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20211103_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='totalamount',
            name='user_linked',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='initial', to=settings.AUTH_USER_MODEL),
        ),
    ]
