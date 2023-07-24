print (" ♦♦ PRINTING A DIMOND ♦♦ ")
print (" Please enter the size od the dimond as an input ")

def line ( khat , max ) :
    stars = 2 * khat + 1
    empty = max - stars 

    for i in range ( int ( empty / 2 )) :
        print (" ", end = "")
        
    for i in range ( stars ) :
        print ("*", end = "")
        
    for i in range ( int ( empty / 2 )) :
        print (" ", end = "")
    
    print ("")

size = int ( input (" Please enter the size of the dimond : "))

most_stars = 2 * size - 1 

for i in range ( size ) :
    line ( i , most_stars  )

for i in range ( size - 2 , -1 , -1 ) :
     line ( i , most_stars )