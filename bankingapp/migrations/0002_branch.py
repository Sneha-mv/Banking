# Generated by Django 4.2.2 on 2023-08-12 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bankingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('area', models.CharField(max_length=250, unique=True)),
                ('dist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bankingapp.district')),
            ],
            options={
                'verbose_name': 'branch',
                'verbose_name_plural': 'branches',
                'ordering': ('area',),
            },
        ),
    ]