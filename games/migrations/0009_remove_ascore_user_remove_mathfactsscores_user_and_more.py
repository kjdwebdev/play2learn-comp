# Generated by Django 5.1 on 2024-11-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0008_alter_gamescore_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ascore',
            name='user',
        ),
        migrations.RemoveField(
            model_name='mscore',
            name='user',
        ),
        migrations.AlterField(
            model_name='gamescore',
            name='game',
            field=models.TextField(choices=[('Math Facts', 'MATH'), ('ANAGRAM', 'Anagram Hunt')], default='MATH'),
        ),
        migrations.DeleteModel(
            name='Ascore',
        ),
        migrations.DeleteModel(
            name='Mscore',
        ),
    ]
