# Generated by Django 5.0.1 on 2024-01-31 17:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_replyingto_reply_commentauthor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='replyTo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='main.post'),
        ),
    ]