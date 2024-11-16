# Generated by Django 5.1.3 on 2024-11-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PolicyUser', '0002_user_age_user_gender_user_residence_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='residence',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]