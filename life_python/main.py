from random import randint

class Cell:
    def __init__(self):
        self.status = 'Dead'
    def is_alive(self):
        if self.status == 'Alive':
            return True
        return False
    def atualiza_status(self, status):
        if status == 'Alive':
            self.status = 'Alive'
        else:
            self.status = 'Dead'
    def tipo_caracter(self):
        if self.is_alive():
            return 'O'
        return '.'

class Board:
    def __init__(self , rows , columns):
        self._rows = rows
        self._columns = columns   
        self._grid = [[Cell() for column_cells in range(self._columns)] 
                        for row_cells in range(self._rows)] #cria um objeto cell para a quantidade de colunas vezes a quantidade de linhas

        self._generate_board()

    def _generate_board(self):
        contador = 0 
        for row in self._grid:
            for column in row:
                chance_number = randint(0,2)
                if chance_number == 1:
                     column.atualiza_status('Alive') #muda o status da célula aleatoriamente para viva ou morta em cada coluna
                # if contador > 0 and contador <6:
                #     column.atualiza_status('Dead')
                #     contador += 1 
                # elif contador > 5 and contador<11:
                #     column.atualiza_status('Dead')
                #     contador += 1 
                # elif contador == 11:
                #     column.atualiza_status('Dead')
                #     contador += 1 
                # elif contador>11 and contador<15:
                #     column.atualiza_status('Alive')
                #     contador += 1 
                # else:
                #     column.atualiza_status('Dead')
                #     contador += 1 

    def draw_board(self):
        print('\n'*10)       #printa a board
        print('Life Game')
        for row in self._grid:
            for column in row:
                print (column.tipo_caracter(),end='')
            print ()  


    def update_board(self):
        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)): #para cada linha
            for column in range(len(self._grid[row])): #cada coluna
                check_vizinho = self._check_vizinho(row , column) #verifica os vizinhos (true e false)
                
                living_neighbours_count = []

                for neighbour_cell in check_vizinho: #para cada vizinho que retorna verifica se esta vivo ou morto
                    if neighbour_cell.is_alive(): 
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self._grid[row][column] #posição da celula(x e y)
                status_main_cell = cell_object.is_alive()#verifica se a minha celula ta viva

                if status_main_cell == True: #se ela estiver viva
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3: #e tiver menos do que dois ou mais que dois vizinhos ela morre
                        gets_killed.append(cell_object)
                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object) #se tiver tres vizinhos volta a vida

        #atualiza os status das células
        for cell_items in goes_alive:
            cell_items.atualiza_status('Alive')

        for cell_items in gets_killed:
            cell_items.atualiza_status('Dead')

    
    
    def _check_vizinho(self, check_row , check_column): #ta dentro da board (lida com os cantos)
        search_min = -1
        search_max = 2
        #pra fazer a pesquisa de vizinhos onde -1 é o anterior  e 2 é o próximo

        neighbour_list = []
        for row in range(search_min,search_max):
            for column in range(search_min,search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column  #começa tecnicamente com todo mundo dentro da board
                
                if (neighbour_row) == check_row and (neighbour_column) == check_column:
                    continue
                elif (neighbour_row) < 0 or (neighbour_row) >= self._rows:
                    continue
                elif (neighbour_column) < 0 or (neighbour_column) >= self._columns:
                    continue
                neighbour_list.append(self._grid[neighbour_row][neighbour_column])
        return neighbour_list

def inicia_jogo():
    user_rows = int(input('Quantas linhas? '))
    user_columns = int(input('Quantas colunas? '))
    game_of_life_board = Board(user_rows,user_columns)
    game_of_life_board.draw_board()
    user_action = ''
    while user_action != 'q':
        continua_question = input('Aperte Enter para continuar')

        if continua_question  == '':
            game_of_life_board.update_board()
            game_of_life_board.draw_board()


inicia_jogo()