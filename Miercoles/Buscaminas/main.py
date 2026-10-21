from Buscaminas import Buscaminas
import random

n = 5
bombas = random.randint(5, 8)

buscaminas = Buscaminas(n, bombas)
buscaminas.mostrar()