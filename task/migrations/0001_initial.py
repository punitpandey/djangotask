# Generated by Django 2.0.2 on 2018-05-22 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classFrom', models.TimeField()),
                ('classTo', models.TimeField()),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('notify_id', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.AddField(
            model_name='schedule',
            name='teacher',
            field=models.ForeignKey(default=1, on_delete='CASCADE', to='task.teacher'),
        ),
    ]