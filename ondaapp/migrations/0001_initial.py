# Generated by Django 4.2 on 2023-04-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('level', models.CharField(max_length=20, null=True)),
                ('type', models.CharField(max_length=20, null=True)),
                ('image_after', models.ImageField(null=True, upload_to='images/')),
                ('image_before', models.ImageField(null=True, upload_to='images/')),
                ('date', models.DateField(null=True)),
            ],
        ),
    ]