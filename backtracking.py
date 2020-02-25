tabela = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def imprime_tabela(tab):

    for i in range(len(tab)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(tab[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                
            if j == 8:
                print(tab[i][j])
            else:
                print(str(tab[i][j]) + " ", end="")

def encontra_vazio(tab):

    for i in range(len(tab)):

        for j in range(len(tab)):
            if tab[i][j] == 0:
                return (i, j) # linha, coluna

    return None

def valido(tab, num, pos):
    #Verifica linha
    for i in range(len(tab[0])):
        if tab[pos[0]][i] == num and pos[1] != i:
            return False

    #Verifica coluna
    for j in range(len(tab)):
        if tab[j][pos[1]] == num and pos[0] != j:
            return False

    #Verificar em que "caixa" estamos 
    caixa_x = pos[1] // 3 
    caixa_y = pos[0] // 3 

    for i in range(caixa_y * 3, caixa_y * 3 + 3):

        for j in range(caixa_x * 3, caixa_x * 3 + 3):
            if tab[i][j] == num and (i, j) != pos:
                return False

    return True

def resolve(tab):
    
    encontra = encontra_vazio(tab)

    if not encontra:
        return True
    else:
        linha, coluna = encontra

    for i in range(1, 10):
        if valido(tab, i, (linha, coluna)):
            tab[linha][coluna] = i

            if resolve(tab):
                return True

            tab[linha][coluna] = 0

    return False

imprime_tabela(tabela)
resolve(tabela)
print(" ")
imprime_tabela(tabela)