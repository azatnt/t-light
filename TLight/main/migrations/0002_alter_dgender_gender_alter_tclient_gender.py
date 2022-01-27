# Generated by Django 4.0.1 on 2022-01-27 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dgender',
            name='gender',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='tclient',
            name='gender',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_gender', to='main.dgender'),
        ),
    ]
