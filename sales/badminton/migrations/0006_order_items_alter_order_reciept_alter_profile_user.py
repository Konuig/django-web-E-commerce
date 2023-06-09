# Generated by Django 4.2 on 2023-04-29 13:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('badminton', '0005_alter_product_type_racket_profile_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.CharField(default='product', max_length=500),
        ),
        migrations.AlterField(
            model_name='order',
            name='reciept',
            field=models.ImageField(upload_to='reciepts'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
