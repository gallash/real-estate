from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Rented, Place
from .forms import RentedForm
from django.contrib import messages


def main(request): # Main page, home page "/"
    print(request.user)
    print(request.user.is_staff)
    print(dir(request.user))
    return render(request, "real_estate/main.html")



# ---- Usuário ------------------------------------
# Isto acontece quando o usuário clica em um botão "requisitar aluguel" que fica na página detalhada
# E se um usuário requisitar vários alugueis
# E se o usuário quiser desistir da requisição?
# Página para o Staff aceitar ou recusar a requisição
@login_required
def rented_creation(request):
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
def place_creation(request):
    if request.user.is_staff:
        # Abrir o formulário para cadastramento de imóveis
        # Verificar se as informações são válidas
        pass
    else:
        return render(request, "real_estate/access-denied.html")

@login_required
def staff_dashboard(request):
    # Aqui o membro de staff poderá 
    # 1. Gerenciar imóveis
    # 2. Aceitar ou rejeitar (rented.user_rental_interest) Esta parte é mesmo necessária?
    pass