# Generated by Django 5.0.6 on 2024-05-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_toy_alter_feeding_options_alter_feeding_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='toys',
            field=models.ManyToManyField(to='main_app.toy'),
        ),
    ]