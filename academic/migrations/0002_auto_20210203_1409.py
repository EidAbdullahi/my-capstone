# Generated by Django 3.0.7 on 2021-02-03 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academic', '0001_initial'),
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guideteacher',
            name='name',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='teacher.PersonalInfo'),
        ),
        migrations.AddField(
            model_name='classregistration',
            name='class_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.ClassInfo'),
        ),
        migrations.AddField(
            model_name='classregistration',
            name='guide_teacher',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='academic.GuideTeacher'),
        ),
        migrations.AddField(
            model_name='classregistration',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.Section'),
        ),
        migrations.AddField(
            model_name='classregistration',
            name='session',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.Session'),
        ),
        migrations.AddField(
            model_name='classregistration',
            name='shift',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='academic.Shift'),
        ),
        migrations.AlterUniqueTogether(
            name='classregistration',
            unique_together={('class_name', 'section', 'shift', 'guide_teacher')},
        ),
    ]
