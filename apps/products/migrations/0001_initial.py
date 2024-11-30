# Generated by Django 5.1.3 on 2024-11-30 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='products')),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
                ('price', models.PositiveSmallIntegerField(default=0)),
                ('published', models.BooleanField(default=False)),
                ('videos', models.FileField(upload_to='videos/')),
                ('description', models.TextField(blank=True, max_length=500)),
                ('weight', models.PositiveSmallIntegerField(default=0)),
                ('length', models.PositiveSmallIntegerField(default=0)),
                ('brand', models.CharField(blank=True, max_length=255)),
                ('product_type', models.CharField(blank=True, max_length=255)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='categories.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]