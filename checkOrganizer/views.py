from django.shortcuts import render

def home_view(request, len, case=""):
    kiss = ""
    if len >= 4:
        seccion = int(len/4)
        letras = ["m","u","a","k"]
        for letra in letras:
            for i in range(seccion):
                kiss += letra

    else:
        kiss = "muak"

    if case.lower()=="mayuscula":
        kiss = kiss.upper()

    return render(request, "home.html", {"kiss":kiss})