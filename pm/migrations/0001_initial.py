# Generated by Django 3.2 on 2021-04-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=255, verbose_name='客户端')),
                ('grade', models.IntegerField(verbose_name='分数')),
            ],
        ),
    ]
