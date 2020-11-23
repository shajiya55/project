# Generated by Django 3.1.3 on 2020-11-22 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20201122_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=70)),
                ('message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='slid',
        ),
    ]
