# Generated by Django 3.1.13 on 2021-11-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20211110_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'Este email ya ha sido registrado.'}, max_length=50, unique=True),
        ),
    ]