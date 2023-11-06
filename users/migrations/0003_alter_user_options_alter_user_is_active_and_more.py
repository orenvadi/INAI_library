# Generated by Django 4.2.6 on 2023-10-29 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-date_joined']},
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterModelTable(
            name='user',
            table='users',
        ),
    ]
