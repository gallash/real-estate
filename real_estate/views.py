from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Rented, Place
from .forms import RentedForm, UserRegistrationForm, HousePlaceForm, AppartmentPlaceForm, KitnetPlaceForm #\
from . import forms
from django.contrib import messages

HOUSE_FIELDS = forms.HOUSE_FIELDS[:-2]
APPARTMENT_FIELDS = forms.APPARTMENT_FIELDS[:-2]
KITNET_FIELDS = forms.KITNET_FIELDS[:-2]



def main(request): # Cuida da paginação
    # print(request.user)
    # print(request.user.is_staff)
    # print(dir(request.user))
    # print(request.session.values())

    # Mostrar todos os imóveis disponíveis
    # Sort por tipo
    # Se der, fazer separar em páginas
    rented_pk_list = [ rented.place.pk for rented in Rented.objects.all() ]
    places = []
    for place in Place.objects.all():
        if place.pk not in rented_pk_list:
            places.append(place)

    context = {'places': places}
    return render(request, "real_estate/main.html", context=context)


def pagination(request, place_id):
    rented_pk_list = [ rented.place.pk for rented in Rented.objects.all() ]
    available_pk_list = [ place.pk for place in Place.objects.all() ]

    ALLOWED = True
    for rented_place in Rented.objects.all():
        if rented_place.place.pk == place_id:
            rented = rented_place
            if rented.status == True:
                ALLOWED = False
                break
    
    if (ALLOWED)and(place_id in available_pk_list):
        place = Place.objects.get(pk=place_id)
        context = {'place': place} # Informação do imóvel que o usuário clicou
        return render(request, "real_estate/pagination.html", context=context)
    elif (request.user.is_staff)and(place_id in available_pk_list):
        place = Place.objects.get(pk=place_id)
        context = {'place': place} # Informação do imóvel que o usuário clicou
        return render(request, "real_estate/pagination.html", context=context)
    else:
        return render(request, "real_estate/access-denied.html")

    # if (place_id not in rented_pk_list)and(place_id in available_pk_list): 
    #     # Se place_id pertencer a algum imóvel disponível
    #     # Não queremos mostrar publicamente onde pessoas moram
    #     place = Place.objects.get(pk=place_id)

    #     context = {'place': place} # Informação do imóvel que o usuário clicou
    #     return render(request, "real_estate/pagination.html", context=context)
    # elif (request.user.is_staff)and(place_id in available_pk_list):
    #     place = Place.objects.get(pk=place_id)
    #     context = {'place': place} 
    #     return render(request, "real_estate/pagination.html", context=context)
    # else:
    #     return render(request, "real_estate/access-denied.html")


# ---- Usuário ------------------------------------
def user_registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Realizar checkups 
            form.save()
            return redirect("login") 
            # Change this in the settings.py file
            # 'login' is already a pre-built system
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, "real_estate/user-registration.html", context=context)


@login_required
def user_dashboard(request):
    # Alterar dados
    # Excluir conta
    # Verificar a solicitação de aluguel
    # Cancelar solicitação de aluguel
    return render(request, "real_estate/user-dashboard.html")


# Isto acontece quando o usuário clica em um botão "requisitar aluguel" que fica na página detalhada
# E se um usuário requisitar vários alugueis
# Adicionar opção do usuário desistir da requisição
# Assim como a opção do usuário deleter sua conta
# Página para o Staff aceitar ou recusar a requisição
# Paginação? Como fazer para mostrar os imóveis
@login_required
def rental_request(request, place_id):
    rented_pk_list = [ rented.place.pk for rented in Rented.objects.all() ]
    if place_id in rented_pk_list: # De novo, não podemos requisitar um imóvel alocado
        return render(request, "real_estate/access-denied.html")

    if request.method == 'POST':
        form = RentedForm(request.POST)
        # valid = all(Place.validate_price(form.data.get("price")))

        if form.is_valid():
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            user_comment = form.cleaned_data.get('user_comment')
            place = Place.objects.get(pk=place_id)
            rented = Rented(user=request.user, place=place, start_date=start_date, end_date=end_date, user_comment = user_comment)
            rented.save()
            messages.success(request, "Solicitação realizada com sucesso. A equipe irá avaliar o pedido.")
        
            return redirect('../../user')
       
    else:
        form = RentedForm()
    
    context = {'form': form}
    return render(request, "real_estate/rental-request.html", context=context)






# ---- Staff --------------------------------------
@login_required
def place_house_registration(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = HousePlaceForm(request.POST) # PlaceForm
            valid = all([Place.validate_price(form.data.get("price"))])
            # O imóvel não é único no banco de dados, retornar erro  
            # Não tive tempo ainda de implementar esta parte do código        
            # for place in Place.objects.all():
            #     # equal = False
            #     for field in HOUSE_FIELDS:
            #         # Não é a solução mais ótima, mas foi a mais rápida de ser feita
            #         if form.data.get(field) == place.__getattribute__(field):
            #             messages.error("O imóvel já foi cadastrado no banco de dados.")
                # place.__dict__
                # if elementos todos forem iguais, tipo estado, cidade, CEP, numero, bloco, nome do prédio, etc baterem, não salvar
                #     messages.error("O imóvel já foi cadastrado no banco de dados.")
                #     pass

            # O imóvel é único
            if (form.is_valid())and(valid):
                form.save()
                place = Place.objects.last()
                place.type_of_place = "Casa"
                place.save()
                messages.success(request, "O imóvel foi cadastrado com sucesso")
        else:
            form = HousePlaceForm()

        context = {'form': form}
        return render(request, "real_estate/house-registration.html", context)
    else:
        return render(request, "real_estate/access-denied.html")


@login_required
def place_appartment_registration(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = AppartmentPlaceForm(request.POST)
            valid = all([Place.validate_price(form.data.get("price"))])

            if (form.is_valid())and(valid):
                form.save()
                place = Place.objects.last()
                place.type_of_place = "Apartamento"
                place.save()
                messages.success(request, "O imóvel foi cadastrado com sucesso")
        else:
            form = AppartmentPlaceForm()

        context = {'form': form}
        return render(request, "real_estate/appartment-registration.html", context)
    else:
        return render(request, "real_estate/access-denied.html")


@login_required
def place_kitnet_registration(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = KitnetPlaceForm(request.POST)
            valid = all([Place.validate_price(form.data.get("price"))])

            if (form.is_valid())and(valid):
                form.save()
                place = Place.objects.last()
                place.type_of_place = "Kitnet"
                place.save()
                messages.success(request, "O imóvel foi cadastrado com sucesso")
        else:
            form = KitnetPlaceForm()

        context = {'form': form}
        return render(request, "real_estate/kitnet-registration.html", context)
    else:
        return render(request, "real_estate/access-denied.html")


@login_required
def staff_dashboard(request):
    if request.user.is_staff:
        # Aqui o membro de staff poderá 
        # 1. Gerenciar imóveis: Mostrar imóveis locados
        # 2. Aceitar ou rejeitar (rented.user_rental_interest) Esta parte é mesmo necessária?
        return render(request, "real_estate/staff-dashboard.html")
    else:
        return render(request, "real_estate/access-denied.html")


@login_required
def request_management(request):
    if request.user.is_staff:
        # Aqui o membro de staff poderá 
        # aceitar ou rejeitar (rented.user_rental_interest)
        
        # Como deletar items?
        # Como implementar botão para aceitar ou remover?
        
        # rented_pk_list = [ rented.place.pk if rented.status is False for rented in Rented.objects.all() ]
        rented_places = []
        for rented_place in Rented.objects.all():
            if rented_place.status is False:
                rented_places.append(rented_place)

        context = {'rented_places': rented_places}
        return render(request, "real_estate/request-management.html", context=context)
    else:
        return render(request, "real_estate/access-denied.html")

@login_required
def accept(request, place_id):
    if request.user.is_staff:
        # Aceitar pedido
        # for rented_place in Rented.objects.all():
        #     if rented_place.place.pk = 
        rented = Rented.objects.get(pk=place_id)
        rented.status = True
        rented.save()

        return redirect("../../request-management") #request_management(request)
    else:
        return render(request, "real_estate/access-denied.html")

@login_required
def refuse(request, place_id):
    if request.user.is_staff:
        # Recusar e excluir pedido
        rented = Rented.objects.get(pk=place_id)
        rented.delete()

        return redirect("../../request-management") # request_management(request)
    else:
        return render(request, "real_estate/access-denied.html")


@login_required
def view_rented(request):
    if request.user.is_staff:
        # Aqui o membro de staff poderá gerenciar imóveis: Mostrar imóveis locados
        rented = []
        for rented_place in Rented.objects.all():
            if rented_place.status is True:
                rented.append(rented_place)
        
        context = {'rented_places': rented}
        return render(request, "real_estate/view-rented.html", context)
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