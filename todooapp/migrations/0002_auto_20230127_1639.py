# Generated by Django 3.1.7 on 2023-01-27 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todooapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2001-01-14'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
