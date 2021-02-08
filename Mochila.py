def main():
    print('Obtener el mayor coste dentro de una mochila con capacidad máxima de 100')
    print('Datos por defecto:')
    # Default data
    arr = [
        {'price': 10, 'weight': 20},
        {'price': 20, 'weight': 30},
        {'price': 30, 'weight': 66},
        {'price': 40, 'weight': 40},
        {'price': 50, 'weight': 20}
    ]
    for idx, art in enumerate(arr):
        print('{}. Costo: ${}; Peso: {} kg'.format(idx + 1, art['price'], art['weight']))
    # To enter data manually
    if input('¿Usar datos predeterminados? (y/n) ') != 'y' :
        arr  = enteries()
    # Assign the divided values of the article
    xArr = getPartArr(makeEmptyArr(arr), arr)

    print('Los artículos que se puede llevar son: ')
    printArticles(xArr)
    return
# Prints all the articles that can be inside the backpack
def printArticles(xArr):
    for idx, value in enumerate(xArr):
        if value != 0: print('{} veces el artículo {}'.format(value, idx+1))
    return
# This is the Alorithm
# Returns the divided values by some criteria defined by voraSelection function
def getPartArr(xArr, arr):
    add = 0
    weight = int(input('Ingrese peso máximo de la mochila (kg): '))
    while add < weight: 
        i = voraSelection(xArr, arr)
        if add + arr[i]['weight'] <= weight:
            xArr[i] = 1
            add = add + arr[i]['weight']
        else: 
            xArr[i] = (weight - add) / arr[i]['weight']
            add = weight
    return xArr
# Returns the values entered by the user
def enteries():
    valid = 'y'
    arr = []
    while True:
        price  = int(input('Ingrese costo: $'))
        weight = int(input('Ingrese peso (kg): '))
        arr.append({'weight':weight, 'price': price})

        valid = input('Costo agregado, ¿Desea agregar otro? (y/n) ')

        while valid != 'y' and valid != 'n' :
            valid = input('Entrada incorrecta, ¿Desea agregar otro? (y/n) ')
        if valid == 'n': break
    return arr

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