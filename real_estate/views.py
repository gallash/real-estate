from django.shortcuts import render


def main(request): # Main page, home page "/"
    return render(request, "real_estate/main.html")