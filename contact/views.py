from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.


def contact(request):
    return render(request, "contact/contact.html")


def contact(request):

    contactForm = ContactForm()
    # instancia del fomrulario
   # print("Tipo de peticion:{}".format(request.method))
    if request.method == "POST":
        contactForm = ContactForm(data=request.POST)
        if contactForm.is_valid():
            name = request.POST.get('name', '')
            phone = request.POST.get('phone', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')
            # eviar correo
            email = EmailMessage(
                "La cafetiera: nuevo mensaje de contacto",
                "DE: {}<{}>\n\nEscribio:\n\n{}".format(name,phone ,email, message),
                "correo_prueba@inbomx.mail.io",
                ["dfrgaa@itsqmet.edu.ec"],
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")
    return render(request, "contact/contact.html", {'contactForm': contactForm})
