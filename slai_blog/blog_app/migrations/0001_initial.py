# Generated by Django 4.0.4 on 2022-05-17 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('text', models.TextField()),
            ],
        ),
    ]
