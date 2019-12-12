import math

class Vectors(object):
	#this class has three attributes for te points of a vector
	def __init__(self,x,y,z):
		# this is the initializing of the points
        # making them floats is important if the user happens to enter a float
		self.x = float(x)
		self.y = float(y)
		self.z = float(z)
	
	def __str__(self):
		#string function to return the points fo the vector
        #returns points in string
        
		return "(%s, %s, %s)"%(self.x,self.y,self.z)
	


	def __add__(self,other):
		# vector made from adding two vector points together
        #returns single vector
        
		return Vectors(self.x+other.x,self.y+other.y,self.z+other.z)
	


	def __sub__(self,other):
		# vector made from subtracting two vectors from each other
        # returns a single vector
		return Vectors(self.x-other.x,self.y-other.y,self.z-other.z)
	


	def __mul__(self,other):
        # multiplies the two vectors by each other 
        # returns a single vector
		return Vectors(self.x*other,self.y*other,self.z*other)
	


	def magnitude(self):
		# uses the math library to square the vector points
        # retirns a single vector
		return math.sqrt((self.x*self.x)+(self.y*self.y)+(self.z*self.z))



#testing init
v1 = Vectors(1,2,3)

#testing print

print("Printing v1")
print("v1 = ",v1)


#testing init
v2 = Vectors(5,5,5)

#testing print
print("Printing v2")
print("v2 = ",v2)
