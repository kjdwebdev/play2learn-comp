# Generated by Django 5.1 on 2024-09-25 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_remove_review_one_vote_per_user_per_game_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.SmallIntegerField(choices=[(5, 'Exceptional'), (4, 'Good'), (3, 'Satisfactory'), (2, 'Unsatisfactory'), (1, 'Unacceptable')]),
        ),
    ]
