# Generated by Django 4.1.4 on 2023-03-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudx', '0010_testing_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='anothertesting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=70, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
                ('summary', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
    ]
