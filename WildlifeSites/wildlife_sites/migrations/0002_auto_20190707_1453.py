# Generated by Django 2.2.2 on 2019-07-07 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wildlife_sites', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxonomyorder',
            old_name='taxclass',
            new_name='class',
        ),
    ]
