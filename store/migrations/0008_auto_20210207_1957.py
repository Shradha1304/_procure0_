# Generated by Django 3.1.2 on 2021-02-07 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20210207_1838'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories '},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'name'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='category_id',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='store.category', verbose_name='category'),
        ),
    ]