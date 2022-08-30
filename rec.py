#create a class for Rectangle
class Rectangle:
    #get Rectangle's attribute
    def __init__(self,len,wid):
        ''' init '''
        self.len = len
        self.wid = wid
    #area
    def area(self):
        ''' calculate Rectangle's area '''
        print("Rectangle's area:")
        return self.len * self.wid
    #perimeter
    def perimeter(self):
        ''' calculate Rectangle's perimeter'''
        print("Rectangle's perimeter:")
        return 2*(self.len + self.wid)
    #points
    def points(self,x,z,y,i):
        '''return points'''
        self.x=x
        self.z=z
        self.y=y
        self.i=i
        return (self.x , self.z , self.y , self.i)
 #\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def __init__(self, len1, wid1, len2, wid2):
        ''' init '''
        self.len1 = len1
        self.wid1 = wid1

        self.len2 = len2
        self.wid2 = wid2

   def __eq__(self):
       return self.len1 == self.len2 and self.wid1 == self.wid2


    