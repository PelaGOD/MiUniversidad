from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings 

def formularioContacto(request):
    return render(request, "Plantillas/formularioContacto.html")

def contactar(request):
    if request.method == "post":
        asunto = request.POST["txtAsunto"]
        mensaje = request.POST["txtMensaje"] + "/ Email:" + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["auxiliar1@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContacto.html")