# Generated by Django 3.1.13 on 2021-11-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Este email ya ha sido registrado.'}, max_length=50),
        ),
    ]
