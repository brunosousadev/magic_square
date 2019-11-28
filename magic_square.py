def sunList(list, size):
    totalSun = 0    
    for index in range(size):
        totalSun+=  list[index]

    return totalSun

def sunColumn(square, column, size):
    totalSun = 0    
    for line in range(size):
        totalSun+= square[line][column]

    return totalSun
    
def verify(square, sumCheck, size):
    line = 0
    column = 0
    for k in range(size):
        line = sunList(square[k], size)
        column = sunColumn(square, k, size)
        if (line != sumCheck) or (column != sumCheck):
            return False
        
    return True

    
def sunDiagonal(square, flag, size):
    totalSun = 0
    if flag:
        column = 0
    else:
        column = size - 1
    for line in range(size):
        totalSun+= square[line][column]
        if flag:
            column+=1
        else:
            column-=1

    return totalSun

def verifyMagicalSquare(square):
    size  = len(square)
    flag  = True
    primary  = sunDiagonal(square, flag, size)
    secondary = sunDiagonal(square, not flag, size)
    if primary != secondary:
        return False
    else:
        if verify(square,primary,size):
            return True
        else:
            return False

def createList(size):
    listAux = []
    for k in range(size):
        listAux.append(-1)
    return listAux

def createSquareEmpty(size):
    square = []
    for k in range(size):
        square.append(createList(size))
    
    return square

def rotate(index, size):
    return index % size    

def createSquare(size):
    square = createSquareEmpty(size)    
    line = 0
    column = (int) (size/2)         
    square[line][column] = 1
    value = 2
    totalValues  = (size*size)
    for k in range(1,totalValues,1):        
        line_previous = line
        column_previos = column
        
        line = rotate(line-1, size)
        column = rotate(column+1, size)

        if square[line][column] != -1:
            line = rotate(line_previous+1, size)
            column = column_previos
        
        square[line][column] = value
        value+=1

    return square


def create():
    while True:
        size = int(input("Enter the desired dimension for the square"))
        if size % 2 != 0:
            break

    square = createSquare(size)
    if verifyMagicalSquare(square):
        for k in range(size):
            print(square[k])


create()
