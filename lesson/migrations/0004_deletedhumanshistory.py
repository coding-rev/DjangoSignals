# Generated by Django 3.2.9 on 2022-03-07 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0003_alter_human_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletedHumansHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('humanId', models.CharField(max_length=12)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
