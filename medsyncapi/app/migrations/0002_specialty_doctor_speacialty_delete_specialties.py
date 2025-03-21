# Generated by Django 5.1.7 on 2025-03-11 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='speacialty',
            field=models.ManyToManyField(related_name='doctors', to='app.specialty'),
        ),
        migrations.DeleteModel(
            name='Specialties',
        ),
    ]
