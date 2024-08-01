# Generated by Django 5.0.7 on 2024-07-31 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Time', models.DateTimeField(auto_now=True)),
                ('Name', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Price', models.FloatField()),
                ('Status', models.BooleanField(default=True)),
                ('Categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.categories')),
            ],
        ),
    ]
