from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect

from .forms import ContactForm

def home_page(request):
    # print(request.session.get("first_name", "Unknown"))
    # request.session['first_name']
    context = {
        "title":"",
        "content":"",

    }
    if request.user.is_authenticated:
        context["premium_content"] = ""
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title":"Obio",
        "content":" Qué nos define"
    }
    return render(request, "home_page.html", context)


def cultura_page(request):
    context = {
        "title":"Cultura Obio",
        "content":" La cultura se amplia con el conocimiento de la gente."
    }
    return render(request, "home_page.html", context)    


def comunidad_page(request):
    context = {
        "title":"Expande la comunidad",
        "content":" Juntos, como sociedad podemos llegar más lejos."
    }
    return render(request, "home_page.html", context)   

def seguimiento_page(request):
    context = {
        "title":"Sigue tu pedido",
        "content":" Tu pedido viene en camino."
    }
    return render(request, "home_page.html", context)   

def cambios_page(request):
    context = {
        "title":"¿Algo salió mal con tu pedido?",
        "content":" Escríbenos, lo podemos resolver."
    }
    return render(request, "home_page.html", context)

def ayuda_page(request):
    context = {
        "title":"Te podemoso ayudar",
        "content":" Mira primero las dudas que comúnmente se preguntan."
    }
    return render(request, "home_page.html", context)        


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contacto",
        "content":" Te responderemos lo más pronto posible.",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Gracias por registrarte"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    # if request.method == "POST":
    #     #print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('content'))
    return render(request, "contact/view.html", context)





def home_page_old(request):
    html_ = """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
      </head>
      <body>
        <div class='text-center'>
            <h1>Hello, world! cvg</h1>
        </div>
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.11.0/umd/popper.min.js" integrity="sha384-b/U6ypiBEHpOf/4+1nzFpr53nxSS+GLCkfwBdFNTxtclqqenISfwAzpKaMNFNmj4" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/js/bootstrap.min.js" integrity="sha384-h0AbiXch4ZDo7tp9hKZ4TsHbi047NrKGLO3SEJAg45jXxnGIfYzk4Si90RDIqNm1" crossorigin="anonymous"></script>
      </body>
    </html>
    """
    return HttpResponse(html_)
