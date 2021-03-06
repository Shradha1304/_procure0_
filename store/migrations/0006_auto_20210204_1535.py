# Generated by Django 3.1.2 on 2021-02-04 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.CharField(default=0, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile',
            field=models.ImageField(upload_to='user/'),
        ),
    ]
