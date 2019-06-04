# Generated by Django 2.2.1 on 2019-06-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full', models.CharField(max_length=150)),
                ('short', models.CharField(max_length=150)),
                ('add', models.DateTimeField()),
                ('cclick', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
