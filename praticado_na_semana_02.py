# -*- coding: utf-8 -*-
"""
Original file is located at
    https://colab.research.google.com/drive/1eifEmefhFzpRm0J0BFRXDFG-ECiLBj9E
"""

def digitar_por_extenso():
    tupla_numerada = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
                      'seis', 'sete', 'oito', 'nove', 'dez',
                      'onze', 'doze', 'treze', 'catorze', 'quinze',
                      'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
                      )
    try:
        numero = int(input('Digite um número: '))
        numero_extenso = tupla_numerada[numero]
        print(f'Número {numero} por extenso: {numero_extenso}')

    except:
        print('Entrada inválida')

digitar_por_extenso()

def times_lista():
    times_list = ('chapecoence', 'bahia', 'ceara', 'atletico', 'fortaleza',
                  'bota-fogo', 'vasco', 'italia', 'roma', 'sao paulo',
                  'itarema','brasil', 'japao', 'barcelona','real madri',
                  'argentina', 'colombia', 'mexico', 'time da praça', 'US'
    )

    return times_list


def primeiros_5(times):
    print(f'{times[0: 5]}')

def ultimos_4(times):
    print(f'{times[-4:]}')

def ordem_alfabetica(times):
    times_em_ordem =  sorted(times)

    return times_em_ordem

def buscar_chapecoence(times):
    for pos, time in enumerate(times):
        if time == 'chapecoence':
           print(f'chapecoence estar na posição {pos + 1}')


def buscar(times):
    try:
        entrada = str(input('Digitar nome do time').strip().lower())
        for pos, time in enumerate(times):
            if entrada == time:

               return pos + 1

    except:

        return 'time não encontrado'

def main_073():
    lista_de_times = times_lista()

    print('''Times uma lista de times
                (a) Exibir lista
                (b) Apenas os 5 primeiros
                (c) Os ultimos 4
                (d) Em que posição ta o chapecoence
                (e) Sair
                (f) Buscar time
    ''')


    while True:
        print('==' * 20)
        resposta_usuario = input('Digite sua resposta: ').strip().lower()[0]

        if resposta_usuario == 'a':

          print(f'Lista de times: {lista_de_times}')

        elif resposta_usuario == 'b':
            primeiros_5(lista_de_times)

        elif resposta_usuario == 'c':
            ultimos_4_times = ultimos_4(lista_de_times)

        elif resposta_usuario == 'd':
            buscar_chapecoence(lista_de_times)

        elif resposta_usuario == 'f':
             buscar_time = buscar(lista_de_times)
             print(f'posição {buscar_time}')

        elif resposta_usuario == 'e':
            print('FIM')
            break

        else:
          print('entrada invalida')

from random import randint

numeros_tupla = ((randint(1, 5)) for _ in range(5))

maior_numero = max(numeros_tupla)
menor_numero = min(numeros_tupla)
print(f'Maior numero: {maior_numero}')
print(f'Menor numero: {menor_numero}')
print(f'Todos os numeros: {numeros_tupla}')

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            print('digite uma entrada válida')


num = tuple(get_int_input('Digitar numero: ') for _ in range(5))

print(f'O valor [9] apareceu: {num.count(9)} vezes')

if 3 in num:
    print(f'A posição do numero [3] é {num.index(3) + 1}')

else:
    print(f' Numero [3] não estar entre os numeros')

numeros_pares = [numero for numero in num if numero % 2 == 0]

print(f'Esses são os numeros pares {numeros_pares}')
print(f'Total de: {len(numeros_pares)}')

produtos = ('barra', 3400,
            'kite23', 4800,
            'kite24', 7500,
            'harness', 1500,
            'helmet', 500,
            'leash', 150
            )

print('--' * 20)
print(f'{"LISTA DE PRODUTOS":^40}')
print('--' * 20)

for posicao in range(0, len(produtos)):
    if posicao % 2 == 0:
       print(f'{produtos[posicao]:.<30}', end='')

    else:
        print(f'R$ {produtos[posicao]:>7.2f}')

palavras = ('casa', 'armario', 'hotel', 'maria',
            'banho', 'varanda', 'mario', 'barra')

for palavra in palavras:
    vogais = []
    for letra in palavra:
        if letra in ['a', 'e', 'i', 'o', 'u']:
            vogais.append(letra)

    print(f'A palavra: {palavra.upper()} tem as letras: {vogais}')

valores = list(int(input('Digitar valor: '))for _ in range(5))

maior_valor = max(valores)
menor_valor = min(valores)

print(f'Maior valor: {maior_valor}')
print(f'Menor valor: {menor_valor}')

for pos, numero in enumerate(valores):
    if maior_valor == numero:
       print(f'A posisao do maior valor: {numero} é: {pos}')

for pos, numero in enumerate(valores):
    if menor_valor == numero:
       print(f'A posisao do menor valor: {numero} é {pos}')

lista_de_numeros = []
while True:
    numero = int(input('Digitar numero: '))
    if numero == 0:

       break

    if numero not in lista_de_numeros:
       lista_de_numeros.append(numero)

lista_de_numeros.sort()
print('Numeros em ordem crescente')
print(lista_de_numeros)

lista_para_numeros = []

for x in range(5):
    num = int(input('Digitar numero: '))

    if num >= 0:
       posicao_inicial = 0
       while posicao_inicial < len(lista_para_numeros) and lista_para_numeros [posicao_inicial] < num: posicao_inicial +=1

       lista_para_numeros.insert(posicao_inicial, num)



print('--' * 20)
print(f'{"Lista de numeros ja em ordem":^40}')
print('--' * 20)
print(lista_para_numeros)

def lista():
    nova_lista = []
    while True:

        try:
            numero = int(input('Digitar numero: '))
            nova_lista.append(numero)

            resposta = int(input('Deseja continuar? [0] / [1]  : ').strip().upper()[0])
            if resposta == 1:

               continue

            if resposta == 0:

                return nova_lista

        except ValueError:
            print('Entrada inválida')


def quantos_numeros_validos(lista):
    return len(lista)


def decrescente_lista(lista_d):
    lista_decre = sorted(lista_d, reverse=True)
    return lista_decre


def crescente_lista(lista):
    return sorted(lista)


def procurar_5(lista):
    vezes = 0

    for numero in lista:
        if 5 == numero:
           vezes += 1

        elif 5 not in lista:

            return 'Numero 5 não digitado'

    return f'Numeero digitado: {vezes} vezes'


def verificar_resposta():
    while True:
        try:
            resposta = input('Digitar opção: ').strip().lower()[0]
            if resposta in ['a', 'b', 'c', 'd', 'e']:

               return resposta

        except:
            print('Entrada inválida')


def comparar_resposta(resposta, lista):
    if resposta == 'a':
       quantidade_numeros_validos = quantos_numeros_validos(lista)
       print(f'Total de numeros validos: {quantidade_numeros_validos}')

    elif resposta == 'b':
         lista_decrecente = decrescente_lista(lista)

         print('--' * 20)
         print(f'{"Lista decrecente":^40}')
         print(lista_decrecente)

    elif resposta == 'c':
         valores_crecentes = crescente_lista(lista)

         print('--' * 20)
         print(f'{"Lista crescente":^40}')
         print(valores_crecentes)

    elif resposta == 'd':
         retorno_da_busca = procurar_5(lista)

         print('--' * 20)
         print(retorno_da_busca)

    elif resposta == 'e':

         print('--' *  20)
         print('FIM')

         return False

    return True

def main_081():
    print('--' * 20)
    print(f'{"Analise de numeros em lista":^40}')
    print('--' * 20)

    lista_dos_numeros = lista()

    print('''
                 (a) Ler quantos numeros foram digitados
                 (b) Mostra lista de valores de forma decrecente
                 (c) Mostra lista de valores de forma crescente
                 (d) Se o valor 5 foi ou não digitado
                 (e) Sair

    ''')
    while True:
        resposta = verificar_resposta()
        if not comparar_resposta(resposta, lista_dos_numeros):

           break

main_081()

def adicionar_num():
    lista_082 = []

    while True:
        try:
            numero = int(input('Digitar numero: [0] para parar '))
            if numero == 0:

              return lista_082

            if numero > 0:
              lista_082.append(numero)

        except ValueError:
            print('apenas numeros')


def criar_lista_par(lista_082):
    lista_par_082 = []

    for numero in lista_082:
        if numero % 2 == 0:
           lista_par_082.append(numero)

    return lista_par_082


def criar_lista_impar(lista_082):
    lista_impar = []

    for numero in lista_082:
        if numero % 2 != 0:
           lista_impar.append(numero)

    return lista_impar


def main_082():
    print('classifique seus numeros entre par e impar')

    numeros = adicionar_num()
    numeros_pares_082 = criar_lista_par(numeros)
    numeros_impar_082 = criar_lista_impar(numeros)

    print('Numeros classificados')
    print('==' * 20)
    print(f'{"Todos os numeros":^30}')
    print('==' * 20)
    print(numeros)
    print('==' * 20)
    print(f'{"Numeros pares":^30}')
    print('==' * 20)
    print(numeros_pares_082)
    print('==' * 20)
    print(f'{"Numeros impar":^30}')
    print('==' * 20)
    print(numeros_impar_082)

main_082()

def verificar_de_parenteses():
    expressao = input('Digitar expressao: ').strip().lower()

    expressao_correta = True
    ordem_parenteses = ''
    cont_aberto = 0
    cont_fechado = 0

    for tecla in expressao:
        if tecla == '(':
           expressao_correta = False
           ordem_parenteses += tecla
           cont_aberto += 1

        if tecla == ')':
           expressao_correta = True
           ordem_parenteses += tecla
           cont_fechado += 1

    if cont_fechado != cont_aberto:
       expressao_correta = False

    print(expressao_correta, ordem_parenteses)

verificar_de_parenteses()

def cadrastro_pessoas():
    pessoas = []
    while True:
        try:
            nome = str(input('Digitar nome: '))
            if nome == '0000':

               break

            peso = float(input('Digitar peso: '))

            pessoa = (nome, peso)
            pessoas.append(pessoa[:])

        except ValueError:
            print('Entrada inválida')

    return pessoas

def pessoas_mais_pesadas(dados):
    lista_por_peso = sorted(dados, key=lambda pessoa: pessoa[1], reverse=True)
    mais_pesados = [lista_por_peso[:2]]

    return mais_pesados


def quantas_pessoas(dados):

    return len(dados)


def pessoas_mais_leves(dados):
    mais_leves = sorted(dados, key=lambda pessoa: pessoa[1])

    return mais_leves[:2]


def main_084():
    pessoas = cadrastro_pessoas()
    pessoas_pesadas = pessoas_mais_pesadas(pessoas)
    quantidade = quantas_pessoas(pessoas)
    mais_leves = pessoas_mais_leves(pessoas)

    print('--' * 20)
    print(f'As pessoas mais pesadas: {pessoas_pesadas}')
    print('--' * 20)
    print(f'As pessoas mais leves: {mais_leves}')
    print('--' * 20)
    print(f'Total de pessoas cadrastradas: {quantidade}')
    print('--' * 20)

def main_085():
    pares = []
    impar = []

    for x in range(5):
        while True:
            try:
                numero = int(input('Digitar numero: '))

                if numero % 2 == 0:
                  pares.append(numero)

                elif numero % 2 != 0:
                    impar.append(numero)

                break
            except ValueError:
                print('Entrada invalida, numero nao contabilizado')

    pares = sorted(pares)
    impar = sorted(impar)
    return f'Os pares: {pares} - impars: {impar}'

import numpy as np

def soma_matriz(matriz):
    return sum(matriz)

def somar_coluna(matriz):
    entrada = int(input(f'Qual coluna vc quer somar? o a {len(matriz) - 1}:  '))

    if entrada < 0 or entrada > len(matriz) - 1:
       print('Coluna invalida')

       return None


    resultado = 0
    for elemento in matriz:
        resultado += elemento[entrada]

    return resultado


def maior_numero_2linha(matriz):
    total = []
    for numero in matriz[1]:
        total.append(numero)

    total = max(total)
    return total


def somar_par(matriz):
    total = 0
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] % 2 == 0:
               total += matriz[linha][coluna]

    return total


def main_086_087():
    matriz = np.zeros((3,3))


    for linha in range(3):
        for coluna in range(3):
            entrada = input('Digitar: ').strip()

            matriz[linha][coluna] = int(entrada)

    print(f'Matriz preenchida: {matriz}')
    print('==' * 30)

    matriz_preenchida = matriz[:]
    soma_total_coluna = somar_coluna(matriz_preenchida)

    print(f'Soma total da coluna: {soma_total_coluna}')
    print('==' * 30)

    maior_numer2 = maior_numero_2linha(matriz_preenchida)
    print(f'O Maior numero da segunda linha: {maior_numer2}')
    print('==' * 30)

    total_matr = soma_matriz(matriz_preenchida)
    print(f'O valor total é: {total_matr} ')
    print('==' * 30)

    somar_pares_matriz = somar_par(matriz_preenchida)
    print(f'A soma dos pares é: {somar_pares_matriz}')
    print('--' * 30)

