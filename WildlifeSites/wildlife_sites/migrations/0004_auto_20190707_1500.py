# Generated by Django 2.2.2 on 2019-07-07 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wildlife_sites', '0003_auto_20190707_1458'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxonomyclass',
            old_name='class',
            new_name='taxclass',
        ),
        migrations.RenameField(
            model_name='taxonomyorder',
            old_name='class',
            new_name='taxclass',
        ),
    ]
