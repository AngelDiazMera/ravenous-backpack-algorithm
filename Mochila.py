# Algorythm: Maximization algorithm on items in a backpack; that is, you
# get the most benefit from a set of items limited by a maximum weight
# Developed by: Jorge Ángel Díaz Mera
#		Rodrigo Cruz Cruz
#		Marco Antonio Rosas Bárcenas
# Universidad Politécnica de Pachuca (c) 2021


import os
import msvcrt

def main():
    os.system('cls');
    print('Funcionamiento\n  Obtiene el mayor coste dentro de una mochila dada una capacidad máxima.\n')
    print('Selección\n  La selección de los artículos está definida por la mejor relación del precio respecto al peso.\n')
    print('Datos por defecto:')
    # Default data, stored by a list
    arr = [
        {'price': 10, 'weight': 20},
        {'price': 20, 'weight': 30},
        {'price': 30, 'weight': 66},
        {'price': 40, 'weight': 40},
        {'price': 50, 'weight': 20}
    ]
    for idx, art in enumerate(arr):
        print('\t{}. Costo: ${}; Peso: {} kg'.format(idx + 1, art['price'], art['weight']))
    # To enter data manually
    if input('\n¿Usar datos predeterminados? (y/n) ') != 'y' :
        arr  = enteries()
    # Assign the divided values of the article
    xArr = getPartArr(makeEmptyArr(arr), arr)

    print('\nLos artículos que se puede llevar son: ')
    printArticles(xArr, arr)
    print("Programa finalizado.\nPresione una tecla para continuar...")
    msvcrt.getch()
    return
# Prints all the articles that can be inside the backpack
def printArticles(xArr, arr):
    total = 0
    for idx, value in enumerate(xArr):
        if value != 0: 
            total += value * arr[idx]['price']
            print('\t{} veces el artículo {}'.format(value, idx+1))

    print('\nTotal ganado: ${}\n'.format(str(total)))
    return
# This is the Alorithm
# Returns the divided values by some criteria defined by voraSelection function
def getPartArr(xArr, arr):
    add = 0
    weight = int(input('\nIngrese peso máximo de la mochila (kg): '))
    while add < weight: 
        # Call the voraSelection function to select an id
        i = voraSelection(xArr, arr) 
        # If the sum of articles is still supported by the maximum weight of the backpack   
        if add + arr[i]['weight'] <= weight:
            xArr[i] = 1
            add = add + arr[i]['weight']
        # When articles need to be divided to be carried in the backpack
        else: 
            xArr[i] = (weight - add) / arr[i]['weight']
            add = weight
    return xArr
# Returns the values entered by the user
def enteries():
    valid = 'y'
    # Empty list
    arr = []
    # Cycle that stops until the user decides to stop entering data of the articles to be evaluated in the algorithm
    print('\nIngrese los datos de los artículos...')
    while True:
        price  = int(input('\tIngrese costo: $'))
        weight = int(input('\tIngrese peso (kg): '))
        arr.append({'weight': weight, 'price': price})

        valid = input('Costo agregado, ¿Desea agregar otro? (y/n)')

        while valid != 'y' and valid != 'n' :
            valid = input('Entrada incorrecta, ¿Desea agregar otro? (y/n) ')
        if valid == 'n': break
    # Returns the list with the new articles data
    return arr

# Fill an array of 0 based on the length of another array.
def makeEmptyArr(arr):
    newArr = []
    for item in arr: newArr.append(0)
    return newArr

# Returns the index of the item which has the biggest relation between price and weight
def voraSelection (xArr, arr):
    maxPer = 0
    sel = 0

    for idx, item in enumerate(arr):
        if xArr[idx] != 0 : continue
        per = item['price'] / item['weight']
        if per > maxPer :
            sel = idx
            maxPer = per
    
    return sel

main()