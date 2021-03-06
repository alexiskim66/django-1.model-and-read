# Generated by Django 3.2 on 2021-04-16 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='writer',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='body',
            new_name='contents',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='pub_date',
            new_name='publishing_date',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title',
        ),
        migrations.AddField(
            model_name='blog',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
