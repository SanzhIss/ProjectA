# Generated by Django 4.0.2 on 2022-04-21 11:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_alter_reguser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reguser',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.MinLengthValidator(10)]),
        ),
    ]
