# Generated by Django 4.2.2 on 2023-06-09 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_principal_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('examcenter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.examcenter')),
                ('name', models.CharField(max_length=35)),
                ('roll', models.IntegerField()),
            ],
            bases=('app.examcenter',),
        ),
    ]
