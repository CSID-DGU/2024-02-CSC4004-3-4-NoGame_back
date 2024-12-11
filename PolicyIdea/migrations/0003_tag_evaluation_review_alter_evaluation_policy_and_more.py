# Generated by Django 5.1.4 on 2024-12-11 12:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PolicyApp', '0004_rating_sentiment_label_rating_sentiment_score'),
        ('PolicyIdea', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='evaluation',
            name='review',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policyidea_evaluations', to='PolicyIdea.policyidea'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_evaluations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='like',
            name='policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policyidea_likes', to='PolicyIdea.policyidea'),
        ),
        migrations.AlterField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_idea_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='policyidea',
            name='policy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='policy_ideas', to='PolicyApp.policy'),
        ),
        migrations.AlterField(
            model_name='policyidea',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_policy_ideas', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='policyimage',
            name='policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policyidea_images', to='PolicyIdea.policyidea'),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='policyidea_scraps', to='PolicyIdea.policyidea'),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_idea_scraps', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='policyidea',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='policy_ideas', to='PolicyIdea.tag'),
        ),
    ]
