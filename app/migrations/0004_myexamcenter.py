# Generated by Django 4.2.2 on 2023-06-09 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_examcenter_candidate'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyExamCenter',
            fields=[
            ],
            options={
                'ordering': ['-id'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('app.examcenter',),
        ),
    ]
