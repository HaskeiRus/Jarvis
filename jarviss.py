# -*- coding: utf-8 -*-

from datetime import datetime
from google import search
import webbrowser
import pyttsx
en = pyttsx.init()
now = datetime.now()
en.say('Ola, tudo bem?')
en.setProperty('voice', b'brazil')
en.runAndWait()
print("")
en.say("Escreva 'Oque você pode fazer?' e vera oque posso fazer")
en.setProperty('voice', b'brazil')
en.runAndWait()
hora = str(now.hour)
minutos = str(now.minute)
dia = str(now.day)
mes = str(now.month)
ano = str(now.year)

en.say(hora)
en.runAndWait()
while True:

  quest = input('Você: ')

  if quest == "Oque você pode fazer?":
    en.say('As perguntas que podem ser feitas são:')
    en.say(' Que horas são? Qual a data de hoje? Escreva (Pesquise por) e depois ira aparecer para voce escrever oque vc quer pesquisar  ')
    en.setProperty("voice", b'brazil')
    en.runAndWait()

  if quest == "Que horas são?":
    en.say(hora)
    en.say("e")
    en.say(minutos)
    en.setProperty('voice', b'brazil')
    en.runAndWait()
  elif quest == 'Qual a data de hoje?':
    en.say(dia)
    en.say("de")
    en.say(mes)
    en.say("De")
    en.say(ano)
    en.setProperty('voice', b'brazil')
    en.runAndWait()
  elif quest == "pesquise por":
    pp = input('pesquisar por: ')
    pesquisa = str(pp)
    en.say("Pesquisando por")
    en.say(pesquisa)
    en.setProperty("voice", b'brazil')
    en.runAndWait()
    webbrowser.open('https://www.google.com.br/webhp#q='+ pp, autoraise=True )
