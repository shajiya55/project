# Generated by Django 3.1.3 on 2020-11-27 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adate', models.DateField()),
                ('ddate', models.DateField()),
                ('room', models.CharField(max_length=3)),
                ('guest', models.CharField(max_length=3)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]
