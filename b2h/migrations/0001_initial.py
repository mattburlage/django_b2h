# Generated by Django 3.0.5 on 2020-05-02 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('kind', models.CharField(choices=[('text', 'Text'), ('number', 'Number'), ('boolean', 'Boolean'), ('paragraph', 'Paragraph')], max_length=32)),
                ('text', models.CharField(blank=True, max_length=128, null=True)),
                ('number', models.FloatField(blank=True, null=True)),
                ('boolean', models.BooleanField()),
                ('paragraph', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of Billboard Chart', max_length=128)),
                ('url', models.URLField(help_text='URL of Chart on Billboard.com')),
                ('positions', models.IntegerField(help_text='Number of positions to fetch')),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('release', models.CharField(max_length=128)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
