# Generated by Django 4.2.4 on 2023-08-23 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '__first__'),
        ('main', '0004_alter_publications_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publications',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='users.profile'),
        ),
    ]