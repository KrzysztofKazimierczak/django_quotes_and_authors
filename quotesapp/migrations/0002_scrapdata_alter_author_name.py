# Generated by Django 4.2.9 on 2024-02-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotesapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(max_length=255)),
                ('dictionary', models.JSONField()),
            ],
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
