# Generated by Django 4.2.9 on 2024-01-25 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_membernew_phoneno'),
    ]

    operations = [
        migrations.AddField(
            model_name='membernew',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='member_photo/'),
        ),
    ]
