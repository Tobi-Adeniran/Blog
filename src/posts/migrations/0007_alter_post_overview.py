# Generated by Django 3.2.13 on 2022-06-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_alter_post_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=models.TextField(),
        ),
    ]