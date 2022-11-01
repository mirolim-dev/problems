class Solution:
    def __init__(self):
        self.main_points = []
        self.additional_point:dict = {'point': None, 'opposite': ''}

    def ___area(self, A:tuple, B:tuple, C:tuple):
        x1, y1 = A
        x2, y2 = B
        x3, y3 = C
        return abs((x1*(y2-y3)+(x2*(y3-y1))+(x3*(y1-y2)))/2.0)

    def give_point(self, point:tuple)->None:
        if len(self.main_points) < 3:
            self.main_points.append(point)
        else:
            print('You cant add points anymore')


    def give_concave_point(self, point:tuple, opposite:str)->None:
        """
            Your points: A -> first input, B -> second input, C -> third input you should 
            choose one point which is opposit concave point
        """

        if opposite == 'A' or opposite == 'B' or opposite == 'C':
            self.additional_point['point'] = point
            self.additional_point['opposite'] = opposite
        else:
            print('you have entered wrong opposite point: You have to enter A or B or C one of them for opposite')
    
    def check_point(self, point:tuple):
        if len(self.main_points) == 3:
            triangle_points_by_dict = {
                'A': 0,
                'B': 1,
                'C': 2
            }
            tr_points = self.main_points.copy()
            TriangelAdditional = None
            D = self.additional_point['point'] # additional point
            A = self.main_points[0]
            B = self.main_points[1]
            C = self.main_points[2]
            TriangelMain = self.___area(A, B, C)
            if D is not None:
                tr_points.remove(tr_points[triangle_points_by_dict[self.additional_point['opposite']]])
                TriangelAdditional = self.___area(D, tr_points[0], tr_points[1])
            Tm1 = self.___area(A, B, point)
            Tm2 = self.___area(A, C, point)
            Tm3 = self.___area(B, C, point)

            Tm_result = Tm1+Tm2+Tm3 == TriangelMain

            Ta1 = self.___area(D, tr_points[0], point)
            Ta2 = self.___area(D, tr_points[1], point)
            Ta3 = self.___area(tr_points[0], tr_points[1], point)

            Ta_result = Ta1 + Ta2 + Ta3 == TriangelAdditional
            
            return Ta_result != Tm_result

        else:
            print("you didn't add 3 points")



shape = Solution()
A = (-2, -1)
B = (-1, 1)
C = (1, 0)
point_Concave = (0, 0)
check_point1 = (0.11, 0.25)
check_point2 = (-1.4, 0.2)

shape.give_point(A)
shape.give_point(B)
shape.give_point(C)
shape.give_concave_point(point=point_Concave, opposite='A')
print(shape.check_point(check_point1))
print(shape.check_point(check_point2))