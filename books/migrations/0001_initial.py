# Generated by Django 4.2.6 on 2023-10-14 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, default='')),
                ('image', models.ImageField(default='media/not_found_404_image/Error404img.png', upload_to='media//books/')),
                ('quantity', models.IntegerField()),
                ('isPossibleToOrder', models.BooleanField(default=True)),
                ('rating', models.FloatField(default=0)),
                ('orders', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='books.category')),
                ('reviews', models.IntegerField(default=0)),
            ],
        ),
    ]
