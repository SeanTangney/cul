# Generated by Django 4.1 on 2022-08-31 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_post_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
