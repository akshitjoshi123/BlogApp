# Generated by Django 3.2.7 on 2021-10-08 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default='Anonymous Users', max_length=20),
        ),
    ]