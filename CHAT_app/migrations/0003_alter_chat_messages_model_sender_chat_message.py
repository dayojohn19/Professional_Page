# Generated by Django 4.2.7 on 2023-11-03 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CHAT_app', '0002_rename_chat_messages_chat_messages_model_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat_messages_model',
            name='sender_chat_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]