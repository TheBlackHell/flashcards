# Generated by Django 4.2 on 2023-07-31 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_description_flashcardset_beschreibung_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flashcardset',
            old_name='ersteller',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='flashcardset',
            old_name='beschreibung',
            new_name='description',
        ),
    ]
