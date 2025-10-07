def row_sums(mat :list[list[float | int]]):
    if not mat: #если нет матрицы
        return [] #возращаем путую матрицу 
    
    rows = len(mat) #подсчет строк 
    cols = len(mat[0]) #подсчет столбцов

    for row in mat: #row временная переменная которая принимает значения из mat
        if len(row) != cols:
            #если длинна матрицы не равна столбцам mat = [
            #[1, 2, 3]
            #[1, 2 ]
            #]  -> в таком случаем ve
            #'длина матрицы это [1, 2 ,3] [1, 2] столбцы это 1 ,1 ; 2, 2 ; 3 ,[]'
            return ValueError #возращаем VE
    
    sums = []
    for row in mat:           # для каждой строки в матрице
        total = sum(row)      # вычисляем сумму элементов строки
        sums.append(total)    # добавляем сумму в список
    return sums

print(row_sums([[1, 2, 3], [4, 5, 6]]))
        
    

    


