#!/usr/bin/python
from os import strerror

#file = input('Enter the name of the file containing the text to parse: ')
file = 'test2'

try:
    stream = open(file, 'rt')
    print(stream.readline())
except IOError as e:
    print('I/O error occurred:', strerror(e.errno))


## Pede o nome do arquivo para o usuario
## Separa linha por linha do arquivo
## Varre cada caractere da linha
    ## Verifica se é uma letra ou acentuação
        ## Converter os diacríticos
        ## Padroniza tudo em minusculo
## Criar um dicionário para armazenar os dados
## Verificar se a letra já existe no dicionário
    ## Criar uma nova entrada se não existir
    ## Somar +1 nos que já existirem
## Ordenar pelo alfabeto os dados
## Criar um arquivo de saida
## Escrever um histograma com o resultado











