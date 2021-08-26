from django.shortcuts import redirect, render

from .forms import FormularioContacto

from django.core.mail import EmailMessage

# Create your views here.


def contacto(request):

    formulario_contacto=FormularioContacto()

    if request.method=="POST":
        formulario_contacto=FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')

            email=EmailMessage(f"Mensaje de {nombre} desde la App de INFO2021", 
            "El usuario \nNombre: {} \nDireccion: {} \nEscribe lo siguiente:\n\n {}".format(nombre,email,contenido),
            "",["gruponro8.info@gmail.com"], reply_to=[email])

            try: 
                email.send() #Si hay un error ocurre o no, lo siguiente

                return redirect('/contacto/?valido')
            except:
                return redirect('/contacto/?novalido')

    return render(request, "contacto/contacto.html", {'miFormulario':formulario_contacto})