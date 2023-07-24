print (" ♦♦ PRINTING A DIMOND ♦♦ ")
print (" Please enter the size od the dimond as an input ")

def line ( max, i ) :

size = int ( input (" Please enter the size of the dimond : "))

most_star = 2 * size - 1 

for i in range ( 1 , most_star + 1 , 2 ) :
   line () 

#for i in range ( most_star - 2 , 0 , -2 ) :
    