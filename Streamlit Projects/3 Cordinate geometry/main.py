

# my task is to create the full fledeged website 
# that can solve any proble related to the 
# co-ordinate gemometry 



# features / types that can be solved
# 1) distance from origin
# 2) point lies on a given line or not
# 3) distance between 2d point and a given line

import streamlit as st 

st.sidebar.markdown('## Units')
page = st.sidebar.selectbox("Choose a Topic:", ["distance from origin", "point lies on a given line", "point lies on a given line"])



class Point:
    def __init__(self,x,y):
        self.x_cord = x
        self.y_cord = y

    # def __str__(self):
    #     # we can print oyr data type in oyr way
    #     return '<{},{}>'.format(self.x_cord , self.y_cord)
    
    def euclidean_distance(self , other):
        # self is first point  x1, y1
        # other is second pint x2, y2
        # distance formula  square_root((x2-x2)pow2 +(y2-y1)pow2)
        return ((self.x_cord - other.x_cord)**2  +  (self.y_cord - other.y_cord)**2)**0.5
    
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))




class line:
    def __init__(self, A, B,C):
        self.A = A
        self.B = B
        self.C = C

    # def __str__(self):
    #     return '{}x +{}y +{} = 0 '.format(self.A ,self.B ,self.C )
    
    # how to check point lies on a line or not
    # point ka x, y lo aur , line ke x, y mai dal do lhs=rhs exist

    def point_on_line(line , point):
        if ((line.A * point.x_cord) +(line.B * point.y_cord )+ line.C) ==0:
            return "lies on the line"
        else:
            return "does not exist"

    def sohortest_path(line ,point):
        return abs(line.A * point.x_cord   +    line.B * point.y_cord   +   line.C )/( line.A**2 + line.B**2)**0.5
    

    def intersection_of_2lines(line ,other):
        if line.A * other.B - line.B * other.A != 0:
            return ("the lines intersect at a single point.")
        elif (line.A * other.B - line.B * other.A == 0) and (line.C * other.B - line.B * other.C == 0):
            return "the lines are coincident (they overlap)."
        elif (line.A * other.B - line.B * other.A == 0) and (line.C * other.B - line.B * other.C != 0):
            return "the lines are parallel and do not intersect."

        
def answers(x,y):
    return p2.distance_from_origin()


if page ==  "distance from origin":
    x = st.text_input("Enter x point co-ordinate :")
    y = st.text_input("Enter y point co-ordinate :")
    p2 = Point(x, y)
    answer =  answers(x, y)
    st.markdown(answer)



    
