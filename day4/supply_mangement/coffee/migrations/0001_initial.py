# Generated by Django 3.2.3 on 2021-05-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('355ml', 'Tall'), ('473ml', 'Grande'), ('591ml', 'Venti')], default='355ml', max_length=10)),
                ('cup_select', models.CharField(max_length=30)),
                ('prodcut_description', models.CharField(default='', max_length=500)),
                ('ice_only', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=0)),
                ('expiry_date', models.DateTimeField()),
            ],
        ),
    ]