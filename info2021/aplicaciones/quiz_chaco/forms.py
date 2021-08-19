from django import forms

from .models import Pregunta
#Aquí creamos el formulario a partir del modelo
class ElegirInlineFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(ElegirInlineFormset, self).clean()
#Lo siguiente nos permite limitar las respuestas correctas, en este caso a 1.
        respuesta_correcta = 0  
        for formulario in self.forms:
            if  not formulario.is_valid():
                return 
            #El cleaned data solamente almacena los datos eliminados.
            if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
                respuesta_correcta += 1

        try:
            assert respuesta_correcta == Pregunta.numero_respuestas_disponibles
#El numero_respuestas_disponibles fue definido en models
        except AssertionError:
                raise forms.ValidationError( 'Exactamente una sola respuesta permitida ')