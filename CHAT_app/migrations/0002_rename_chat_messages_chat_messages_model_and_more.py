# Generated by Django 4.2.7 on 2023-11-03 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CHAT_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Chat_Messages',
            new_name='Chat_Messages_Model',
        ),
        migrations.RenameModel(
            old_name='Chat_Room',
            new_name='Chat_Room_Model',
        ),
    ]