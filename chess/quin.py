class Quin:
    """
        You should create object with default positions x:int, y:int
    """

    def __init__(self, x:int, y:int):
        self.default_x = x 
        self.default_y = y
        self.result_position = None
        self.x_cordianatas = [x for x in range(1, 9)]
        self.y_cordianatas = [y for y in range(1, 9)]


    def horizontal_moves(self)->list:
        moves_chances = [(x, self.default_y) for x in self.x_cordianatas if x != self.default_x]
        return moves_chances

    
    def vertical_moves(self)->list:
        moves_chances = [(self.default_x, y) for y in self.y_cordianatas if y != self.default_y]
        return moves_chances


    def right_arrow_moves(self)->list:
        """↗️ moves"""
        moves_chances = []
        if self.default_x + self.default_y > 2:
            for x in self.x_cordianatas:
                for y in self.y_cordianatas:
                    if x != y and x+y == self.default_x+self.default_y:
                        moves_chances.append((x, y))
        return moves_chances


    def lef_arrow_moves(self)->list:
        """↖️ moves"""
        moves_chances = []
        def by_decriese_moves()->list:
            m_ch = []
            steps = 1
            while True:
                if self.default_x-steps < 1 or self.default_y-steps < 1:
                    break
                else:
                    m_ch.append((self.default_x-steps, self.default_y-steps))
                    steps += 1
            return m_ch
        
        def by_increase_moves()->list:
            m_ch = []
            steps = 1
            while True:
                if self.default_x+steps > 8 or self.default_y+steps > 8:
                    break
                else:
                    m_ch.append((self.default_x+steps, self.default_y+steps))
                    steps += 1
            return m_ch
        
        if self.default_x == 1 or self.default_y == 1:
            pass
        else:
            moves_chances.extend(by_decriese_moves())
        if self.default_x == 8 or self.default_y == 8:
            pass
        else:
            moves_chances.extend(by_increase_moves())
        return moves_chances


    def all_move_chances(self)->list:
        """This function returns Quin's all moveable oportunities by the cordinates"""
        moves_list = []
        operations_list = [self.horizontal_moves(), self.vertical_moves(), self.lef_arrow_moves(), self.right_arrow_moves()]
        for operation in operations_list:
            moves_list.extend(operation)

        return moves_list


quin = Quin(1, 5)
print(quin.all_move_chances())

  