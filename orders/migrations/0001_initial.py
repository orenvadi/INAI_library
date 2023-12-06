# Generated by Django 4.2.6 on 2023-12-01 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Ожидает проверки', 'Ожидает проверки'), ('В обработке', 'В обработке'), ('Выполнен', 'Выполнен'), ('Отклонено', 'Отклонено')], default='Ожидает проверки', max_length=50)),
                ('comment', models.TextField(blank=True, default='')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('due_time', models.DateTimeField(null=True, validators=[orders.models.validate_due_date])),
                ('books', models.ManyToManyField(to='books.book')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
                'ordering': ['-created_time'],
            },
        ),
    ]
