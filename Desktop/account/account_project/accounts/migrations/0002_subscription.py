# Generated by Django 5.1.1 on 2024-10-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('monthly_price', models.CharField(max_length=255)),
                ('yearly_price', models.CharField(max_length=255)),
            ],
        ),
    ]
