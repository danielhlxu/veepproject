# Generated by Django 2.1.5 on 2019-03-14 21:18

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donorname', models.CharField(max_length=200)),
                ('invoicenum', models.CharField(default='2019', max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('number_of_donations', models.IntegerField(default=1)),
                ('donor_email', models.CharField(max_length=1000)),
                ('donor_phone', models.CharField(max_length=100)),
                ('donor_address', models.CharField(max_length=2000)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='donors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluated_at', models.DateTimeField(auto_now_add=True)),
                ('evaluated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evaluation', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehousenum', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('manufacturer', models.CharField(max_length=300)),
                ('item_type', models.CharField(max_length=200)),
                ('power_test', models.CharField(choices=[('Y', 'Pass.'), ('N', 'Fail.')], default='--', max_length=100)),
                ('starter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_test', models.CharField(choices=[('Y', 'Pass.'), ('N', 'Fail.')], default='--', max_length=100)),
                ('tested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_of_item', models.CharField(max_length=1000)),
                ('attribute_name', models.CharField(max_length=2000)),
            ],
        ),
    ]