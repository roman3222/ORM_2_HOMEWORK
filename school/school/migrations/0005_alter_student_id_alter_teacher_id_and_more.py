# Generated by Django 4.1.7 on 2023-03-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_alter_teacherstudent_options_alter_student_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='teacherstudent',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
