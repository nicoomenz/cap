# Generated by Django 4.1.4 on 2022-12-30 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Redirect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_created_at', models.DateTimeField(auto_now_add=True)),
                ('_update_at', models.DateTimeField(auto_now=True)),
                ('_key', models.CharField(db_index=True, max_length=36)),
                ('_url', models.CharField(max_length=50)),
                ('_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
