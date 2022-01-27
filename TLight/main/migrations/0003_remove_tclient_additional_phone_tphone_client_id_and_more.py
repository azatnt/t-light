# Generated by Django 4.0.1 on 2022-01-27 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_dgender_gender_alter_tclient_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tclient',
            name='additional_phone',
        ),
        migrations.AddField(
            model_name='tphone',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='main.tclient'),
        ),
        migrations.AlterField(
            model_name='tlegalentitydepartment',
            name='id_department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='dept_legal', to='main.tdepartment'),
        ),
        migrations.AlterField(
            model_name='tlegalentitydepartment',
            name='id_legal_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='legal_dept', to='main.tlegalentity'),
        ),
    ]