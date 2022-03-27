from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Rented, Place
from .forms import RentedForm, UserRegistrationForm
from django.contrib import messages



def main(request): # Main page, home page "/"
    print(request.user)
    print(request.user.is_staff)
    print(dir(request.user))
    return render(request, "real_estate/main.html")



# ---- Usuário ------------------------------------
def user_registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Realizar checkups 
            # save
            return redirect("login") # Change this in the settings.py file
            # 'login' is already a pre-built system
            # pass
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, "real_estate/user-registration.html", context=context)



@login_required
def user_dashboard(request):
    return render(request, "real_estate/user-dashboard.html")



# Isto acontece quando o usuário clica em um botão "requisitar aluguel" que fica na página detalhada
# E se um usuário requisitar vários alugueis
# E se o usuário quiser desistir da requisição?
# Página para o Staff aceitar ou recusar a requisição
@login_required
def rental_request(request):
    if request.method == 'POST':
        form = RentedForm(request.POST)
        valid = all(Place.validate_price(form.data.get("price")))

        if (form.is_valid() and valid):
            # form.save()
            
            messages.success(request, "Requisição realizada com sucesso. A equipe irá avaliar o pedido.")
        
            # Dashboard do usuário
            return render(request, "real_estate/user-dashboard.html")
        # else 
        
    else:
        form = RentedForm()
    
    context = {'form': form}
    return render(request, "real_estate/request-rental.html", context=context)






# ---- Staff --------------------------------------
@login_required
def place_registration(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = Place(request.POST) # PlaceForm
            valid = all(Place.validate_price(form.data.get("price")))
            # Abrir o formulário para cadastramento de imóveis
            # Verificar se as informações são válidas
            # O imóvel não é único no banco de dados, retornar erro
            # Confirmei que posso comprar listas assim: 
            #       form.lista_de_todos_elementos_do_imóvel = lista de todos os elems dos imóveis no DB

            # O imóvel é único
            if (form.is_valid())and(valid):
                # form.save()
                # messages.success("O imóvel foi salvo com sucesso")
                # return 
                pass        
        else:
            form = Place()

        context = {'form': form}
        return render(request, "real_estate/place-registration.html")
    else:
        return render(request, "real_estate/access-denied.html")

@login_required
def staff_dashboard(request):
    if request.user.is_staff:
        # Aqui o membro de staff poderá 
        # 1. Gerenciar imóveis
        # 2. Aceitar ou rejeitar (rented.user_rental_interest) Esta parte é mesmo necessária?
        pass
    else:
        return render(request, "real_estate/access-denied.html")










# Algumas coisas 
# 1. eu posso acessar rented direto do usuário: user.rented.place.price por exemplo
# 2. preciso criar htmls, views e tbm atualizar o banco de dados quando terminar o modelo
# ^ para criação de páginas estáticas de registro de imóveis
# 3. preciso criar página do usuário escolher o imóvel para alugar
# 4. preciso construir a página do staff de gerenciar as solicitações
# 5. CRUD. Tbm dar opção de deleter o usuário
# 6. Style com CSS