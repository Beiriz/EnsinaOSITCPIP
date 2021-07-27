#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Jose Beiriz - josebeiriz@gmail.com - 26/07/2021
'''# -*- coding: latin-1 -*-'''
#-----------------------------------------------------------------------
__author__ = 'Beiriz'
__version__= 1.100
#-----------------------------------------------------------------------
import sys
import os
import random
import secrets
from time import sleep

class modelo:
  camada = 0
  nome = ''
  pdu = ''
  tipo = ''

  def __init__(self):
    print("ERRO! A classe modelo deve ser instanciada com os atributos: camada, nome,  pdu e tipo")
    sys.exit(1)

  def __init__(self, camada, nome, pdu, tipo):
    self.camada = camada
    self.nome = nome
    self.pdu = pdu
    self.tipo = tipo

  def get_camada(self):
    return self.camada
  def get_nome(self):
    return self.nome
  def get_pdu(self):
    return self.pdu
  def get_tipo(self):
    return self.tipo

def imprime_cabecalho(txt_score=''):
  sleep(1)
  os.system('cls' if os.name == 'nt' else 'clear')
  retorno = "\n%s\n### %s - DITADO DOS MODELOS OSI E TCP/IP - v%s ###\n%s\n" %(70*'#',__author__, __version__,70*'#')
  if txt_score!='':
    retorno = ("%s\n%s\n"%(retorno,txt_score))
  retorno = ("%s\nEnvie 'x' como resposta para encerrar...\n"%retorno)
  return (retorno)

print (imprime_cabecalho())

lista = []
resposta = ""
qt_perguntas = 0
qt_acertos = 0
score = 0.0

lista.append( modelo(1, 'Física', 'bit', 'OSI') )
lista.append( modelo(2, 'Enlace', 'quadro', 'OSI') )
lista.append( modelo(3, 'Rede', 'pacote', 'OSI') )
lista.append( modelo(4, 'Transporte', 'segmento', 'OSI') )
#lista.append( modelo(4, 'Transporte/TCP', 'segmento', 'OSI') )
#lista.append( modelo(4, 'Transporte/UDP', 'datagrama', 'OSI') )
lista.append( modelo(5, 'Sessão', 'sincronização', 'OSI') )
lista.append( modelo(6, 'Apresentação', 'sintaxe', 'OSI') )
lista.append( modelo(7, 'Aplicação', 'dado', 'OSI') )

lista.append( modelo(1, 'Acesso', 'quadro', 'TCP/IP') )
lista.append( modelo(2, 'Internet', 'pacote', 'TCP/IP') )
lista.append( modelo(3, 'Transporte', 'segmento', 'TCP/IP') )
lista.append( modelo(4, 'Aplicação', 'dado', 'TCP/IP') )

print ("\nCARREGA AS CAMADAS...\n")

for objeto in lista:
  print ("- CAMADA %i DO %s - Nome=%s - PDU=%s" % ( objeto.get_camada(), objeto.get_tipo(), objeto.get_nome(), objeto.get_pdu() ) )

print ("\nTecle [ENTER] para começar...")
resposta = input()

while resposta.lower() !='x':
  pergunta = ''
  resposta = ''
  resposta_correta = ''
  objeto = None
  print(imprime_cabecalho("\n\tSCORE: %i/%i = %.2f%s\t\n" % (qt_acertos,qt_perguntas, score, '%')))
  objeto = random.choice(lista)
  modalidades = ['camada', 'nome', 'pdu']
  modalidade = secrets.choice(modalidades)
  if modalidade == 'camada':
    pergunta = "Qual o número da camada %s no modelo %s" % (objeto.get_nome(), objeto.get_tipo())
    resposta_correta = ("%i" % (objeto.get_camada()));
  elif modalidade =='pdu':
    pergunta = "Qual o nome do PDU da camada %s no modelo %s" % (objeto.get_nome(), objeto.get_tipo())
    resposta_correta = objeto.get_pdu();
  elif modalidade =='nome':
    pergunta = "Qual o nome da camada %i no modelo %s" % (objeto.get_camada(), objeto.get_tipo())
    resposta_correta = objeto.get_nome();
  #print ("- CAMADA %i DO %s - Nome=%s - PDU=%s" % ( objeto.get_camada(), objeto.get_tipo(), objeto.get_nome(), objeto.get_pdu() ) )
  print ("Pergunta %i) %s?" % (qt_perguntas, pergunta))
  resposta = input()
  if resposta !='x':
    qt_perguntas+=1
    print ("%s- Resposta: '%s'\n%s- Correta: '%s'" % ( 2*' ', resposta, 2*' ', resposta_correta) )
    if resposta_correta.lower() == resposta.lower() or ("%ss"%resposta_correta.lower()) == resposta.lower():
      qt_acertos+=1
      print ("\n\t*** ACERTOU! ***\t")
    else:
      print ("\n\t*** ERROU! ***\t")
  if qt_acertos > 0:
    score = float(qt_acertos*100/qt_perguntas);
print ("\n\tFIM!\t\n\tSCORE FINAL: %i/%i = %.2f%s\t\n" % (qt_acertos,qt_perguntas, score, '%') )
sys.exit(0)