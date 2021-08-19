# Generated by Django 3.0.5 on 2021-08-19 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quiz_chaco', '0007_auto_20210817_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElegirRespuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, null=True, verbose_name='¿Es esta la pregunta correcta?')),
                ('titulo', models.TextField(verbose_name='Texto de la respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='PreguntasRespondidas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correcta', models.BooleanField(default=False, verbose_name='¿Es la respuesta correcta?')),
                ('puntaje_obtenido', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='puntaje obtenido')),
            ],
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='pregunta',
        ),
        migrations.AddField(
            model_name='pregunta',
            name='max_puntaje',
            field=models.DecimalField(decimal_places=2, default=3, max_digits=6, verbose_name='Maximo Puntaje'),
        ),
        migrations.RenameModel(
            old_name='perfilUsuario',
            new_name='QuizUsuario',
        ),
        migrations.DeleteModel(
            name='Intentos_respuesta',
        ),
        migrations.DeleteModel(
            name='Respuesta',
        ),
        migrations.AddField(
            model_name='preguntasrespondidas',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_chaco.Pregunta'),
        ),
        migrations.AddField(
            model_name='preguntasrespondidas',
            name='quizUser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz_chaco.QuizUsuario'),
        ),
        migrations.AddField(
            model_name='preguntasrespondidas',
            name='respuesta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='intentos', to='quiz_chaco.ElegirRespuesta'),
        ),
        migrations.AddField(
            model_name='elegirrespuesta',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opciones', to='quiz_chaco.Pregunta'),
        ),
    ]
