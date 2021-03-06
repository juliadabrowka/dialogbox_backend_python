# Generated by Django 3.2.5 on 2021-10-23 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('date', models.DateField(auto_now=True)),
                ('choices', models.CharField(choices=[('ACTIVE', 'Active'), ('SOLD', 'Sold')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=300)),
                ('title', models.TextField()),
                ('image', models.ImageField(upload_to='uploads/')),
                ('date', models.DateField(auto_now=True)),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to='collage_app.serie')),
            ],
        ),
    ]
