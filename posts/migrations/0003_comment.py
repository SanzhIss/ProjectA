# Generated by Django 4.0.2 on 2022-03-29 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_population_city_name_status_city_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('comment_text', models.CharField(max_length=50, null=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
