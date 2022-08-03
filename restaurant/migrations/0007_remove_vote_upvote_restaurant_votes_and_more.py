# Generated by Django 4.0.6 on 2022-08-03 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_vote'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='upvote',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='votes',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vote',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote', to='restaurant.restaurant'),
        ),
    ]