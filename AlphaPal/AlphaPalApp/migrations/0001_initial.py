# Generated by Django 3.2.6 on 2021-09-16 10:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlphaReportTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('client_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('user_image', models.ImageField(blank=True, default='default.png', null=True, upload_to='')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('location', models.ManyToManyField(blank=True, to='AlphaPalApp.AlphaReportTable')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('transaction', models.DateTimeField(auto_now_add=True)),
                ('transaction_amount', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('transaction_type', models.CharField(choices=[('Checking', 'Checking'), ('E-wallet', 'E-wallet'), ('Deposit', 'Deposit'), ('Cashing', 'Cashing')], max_length=200, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlphaPalApp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('account_number', models.IntegerField()),
                ('account_type', models.CharField(choices=[('checking', 'Checking'), ('business', 'Business'), ('savings', 'Savings'), ('cashpal', 'Cashpal')], max_length=200)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AlphaPalApp.client')),
            ],
        ),
    ]
