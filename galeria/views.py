from django.shortcuts import render



def index(resquest):
    return render(resquest, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')
