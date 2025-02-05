# Generated by Django 5.0.3 on 2024-03-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0007_rename_state_appointment_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField(unique=True)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=250)),
            ],
        ),
    ]
