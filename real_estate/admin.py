from django.contrib import admin
from .models import Place, Rented

# Admin User: inatel
# Admin Pass: r34l3st4t3
#
# Staff User: staff
# Staff Pass: r34lt0r
#
# Client 1 User: Gustavo
# Client 1 Pass: cl13nt31
# Client 1 está com aluguel em dia
#
# Client 2 User: Vitoria
# Client 2 Pass: cl13nt32
# Client 2 está com aluguel dentro de 30 dias até expirar
# 
# O avaliador da Inatel poderá criar uma conta simples para verificar como funciona o processo


admin.site.register(Place)
admin.site.register(Rented)