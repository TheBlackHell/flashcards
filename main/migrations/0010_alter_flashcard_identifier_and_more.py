# Generated by Django 4.2 on 2024-03-26 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_flashcardset_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='identifier',
            field=models.CharField(max_length=80, unique=True),
        ),
        migrations.AlterField(
            model_name='flashcardset',
            name='identifier',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]