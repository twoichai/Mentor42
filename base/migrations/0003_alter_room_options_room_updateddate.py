# Generated by Django 5.1.3 on 2024-11-27 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_topic_room_host_message_room_topic'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
        migrations.AddField(
            model_name='room',
            name='updatedDate',
            field=models.DateField(auto_now=True),
        ),
    ]
