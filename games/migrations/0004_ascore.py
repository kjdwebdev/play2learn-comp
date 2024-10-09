# Generated by Django 5.1 on 2024-10-07 18:58

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_anagramhuntscores_slug_mathfactsscores_slug'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ascore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=1)),
                ('max_number', models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(8), django.core.validators.MinValueValidator(5)])),
                ('operation', models.CharField(max_length=30)),
                ('end_time', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ascore', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]