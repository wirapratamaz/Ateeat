# Generated by Django 4.1.4 on 2023-02-01 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SellerUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=320)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=150)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]