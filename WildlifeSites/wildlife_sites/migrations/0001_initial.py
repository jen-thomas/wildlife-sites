# Generated by Django 2.2.2 on 2019-07-07 14:51

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('position', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('location', models.CharField(max_length=512)),
                ('country', models.CharField(max_length=256)),
                ('notes', models.TextField(blank=True, max_length=1024, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SourceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaxonomyClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TimeOfYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UriType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Uri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uri', models.CharField(max_length=1024)),
                ('uri_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wildlife_sites.UriType')),
            ],
        ),
        migrations.CreateModel(
            name='TaxonomyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.CharField(max_length=256)),
                ('taxclass', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wildlife_sites.TaxonomyClass')),
            ],
        ),
        migrations.CreateModel(
            name='Taxonomy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latin_name', models.CharField(max_length=255, unique=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='wildlife_sites.TaxonomyOrder')),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name_english', models.CharField(blank=True, max_length=1024, null=True)),
                ('common_name_catalan', models.CharField(blank=True, max_length=1024, null=True)),
                ('common_name_spanish', models.CharField(blank=True, max_length=1024, null=True)),
                ('latin_name', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='wildlife_sites.Taxonomy')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('author', models.CharField(blank=True, max_length=256, null=True)),
                ('reference', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wildlife_sites.Reference')),
                ('source_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wildlife_sites.SourceType')),
                ('uri', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wildlife_sites.Uri')),
            ],
        ),
        migrations.CreateModel(
            name='SiteVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wildlife_sites.Site')),
                ('source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wildlife_sites.Source')),
                ('species', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wildlife_sites.Species')),
                ('time_of_year', models.ManyToManyField(blank=True, to='wildlife_sites.TimeOfYear')),
            ],
        ),
        migrations.AddField(
            model_name='reference',
            name='reference_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wildlife_sites.ReferenceType'),
        ),
    ]
