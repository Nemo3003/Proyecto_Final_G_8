# Generated by Django 3.2.6 on 2021-09-02 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0007_auto_20210901_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elegirrespuesta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pregunta',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='preguntasrespondidas',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='quizusuario',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]