# Generated by Django 3.2.16 on 2023-04-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('CUSTOMER', 'Клиенту'), ('TECHNICIAN', 'Техник'), ('MASTER', 'Мастер'), ('WORKER', 'Слесорь')], default='CUSTOMER', max_length=50),
        ),
    ]
