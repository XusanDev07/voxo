# Generated by Django 5.1.3 on 2024-12-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='orders/', verbose_name='Order Image')),
                ('order_code', models.CharField(max_length=20, unique=True, verbose_name='Order Code')),
                ('payment_method', models.CharField(choices=[('card', 'Card'), ('cash', 'Cash'), ('paypal', 'PayPal')], default='cash', max_length=10, verbose_name='Payment Method')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')], default='pending', max_length=20, verbose_name='Order Status')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Order Amount')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
        ),
    ]
