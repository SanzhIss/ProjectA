# Generated by Django 4.0.2 on 2022-04-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_user_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(blank=True)),
                ('picture', models.ImageField(default='default value', upload_to='')),
                ('author', models.CharField(default='anonymous', max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('describe', models.TextField(default='DataFleir Django tutorials')),
            ],
            options={
                'verbose_name': 'Мақала',
                'verbose_name_plural': 'Мақалалар',
            },
        ),
    ]