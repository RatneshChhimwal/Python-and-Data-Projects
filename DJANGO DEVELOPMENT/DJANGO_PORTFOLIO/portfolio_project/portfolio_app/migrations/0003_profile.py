# Generated by Django 5.1 on 2024-09-02 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0002_projectimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='user_image/')),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
