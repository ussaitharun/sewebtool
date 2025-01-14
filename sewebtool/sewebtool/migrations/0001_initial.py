# Generated by Django 4.1.7 on 2024-12-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TransitAgency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the long name for the Transit Agency, Max 50 characters', max_length=50)),
                ('abbreviation', models.CharField(help_text='Enter the abbreviation for the Transit Agency, Max 10 characters', max_length=10)),
                ('city', models.CharField(help_text='Enter the City for the Transit Agency, Max 20 characters', max_length=20)),
                ('state', models.CharField(help_text='Enter the 2 letter abbreviation for the state where the Transit Agency is located', max_length=2)),
                ('customer_account_number', models.CharField(help_text='Enter the customer account num', max_length=20)),
            ],
        ),
    ]
