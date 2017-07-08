# -*- coding: utf-8 -*-

from datetime import datetime
from google import search
import webbrowser
print('As perguntas que podem ser feitas são: Que horas são? Qual a data de hoje? Escreva (Pesquise por) e depois ira aparecer para voce escrever oque vc quer pesquisar  ')

while True:
  now = datetime.now()
  quest = input('Você: ')

  if quest == "Que horas são?":
    print("são: ", now.hour, ':', now.minute)
  elif quest == 'Qual a data de hoje?':
    print('é', now.day, 'de', now.month, 'de', now.year)
  elif quest == "pesquise por":
    pp = input('pesquisar por: ')
    webbrowser.open('https://www.google.com.br/webhp#q='+ pp, autoraise=True )