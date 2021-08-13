from django.http import HttpResponse

def saludo(request):

    return HttpResponse("Holaaaa, primera pagina con django :3")
    