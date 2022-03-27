from django.db import models
# Use 'django-address'?
# use 'django-cities'?
from django.contrib.auth.models import User
import datetime

# Problemas em aberto:
# 1. Adicionar maneira de verificar existência do endereço 
# 2. Adicionar verificação de choque de endereço. Endereços devem ser únicos
# 3. Adicionar Field para Fotos?
#
# Tentar botar Choices

# types = ['Apartamento', 'Casa', 'Kitnet']



class Place(models.Model):
    STATE_CHOICES = [
        ('SP', "São Paulo"),
        ('RS', "Rio Grande do Sul")
    ]

    TYPE_CHOICES = [
        ('Apto', 'Apartamento'),
        ('Casa', 'Casa'),
        ('Kit', 'Kitnet')
    ]

    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    city = models.CharField(max_length=30)

    # address = models.CharField(max_length=50) # Informação adicional, como N° de apartamento, de casa, andar
    street = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=30)
    garage = models.IntegerField()
    
    # Casa
    # Somente os acima

    # Apartamento
    # Kitnet
    building_name = models.CharField(max_length=30)
    floor = models.CharField(max_length=10)
    bloc = models.CharField(max_length=30)
    appartment_number = models.CharField(max_length=30)
    

    

    description = models.CharField(max_length=200) # Informação extra, como pontos de referência, quantos
    type_of_place = models.CharField(max_length=10, choices=TYPE_CHOICES)
    price = models.FloatField()
    # Código do imóvel = pk do objeto

    def validate_type(self):
        types = [ self.TYPE_CHOICES[n][0] for n in range(self.TYPE_CHOICES) ] # Comment 'types' outside the classes
        valid = True if self.type_of_place in types else False
        return valid

    def validate_price(self):
        # Válido se positivo e com no máx 2 casa decimais
        is_positive = True if (self.price >= 0) else False
        correct_decimals = True if (self.price*100 % 1 == 0) else False 
        valid = all([is_positive,correct_decimals])
        return valid

    # def available_places(self): # Place - Rented
    #     self.objects.all()
    #     pass



class Rented(models.Model):
    # O modelo Rented (alugado) existirá no ato da confirmação do aluguel
    # O objeto será deletado caso de 
    #   1. o usuário e/ou o registro do imóvel seja(m) deletado(s), 
    #   2. na deleção manual do registro
    #   3. período expirou e não houve renovação


    # I have to create the rented object like this: rented = Rented(user=user, place=place)

    user = models.OneToOneField(User, on_delete=models.CASCADE) # Usuário que está logado no ato do aluguel
    place = models.OneToOneField(Place, on_delete=models.CASCADE) # Imóvel em questão
    # user_pk
    # place_pk
    # start_period = datetime.date()
    start_date = models.DateField(default=datetime.date.today())
    end_date = models.DateField(default= datetime.date.today() + datetime.timedelta(days=365))
    # end_period   # datetime obj? 
    

# class RentalRequest(models.Model):
# Esta classe é criada quando o usuário realiza uma requisição?
# Ou simplesmente criar uma variável no Rented, chamada permission_from_staff?
#     user = User
