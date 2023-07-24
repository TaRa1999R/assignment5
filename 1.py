print (" ♟♟ PRINT A CHESS PAGE ♟♟ ")
print (" Please enter the number of rows and column as input ")

def khat_fard (column) :
    baqi_mande = column % 2
    if baqi_mande == 0 :
        for i in range ( int( column / 2 )) :
            print ("#", end = "*" )
        print ("")
    
    else :
        for i in range ( int( column / 2 ) ) :
            print ("#", end = "*" )
        print ("#")
   

def khat_zoj (column) :
    baqi_mande = column % 2
    if baqi_mande == 0 :
        for i in range ( int( column / 2 )) :
            print ("*", end = "#" )
        print ("")
    
    else :
        for i in range ( int( column / 2 ) ) :
            print ("*", end = "#" )
        print ("*")
    


row = int ( input (" Please enter the number of rows : "))
column = int ( input (" Please enter the number of columns : "))

baqi_mande = row % 2 
if baqi_mande == 0 :
    for i in range ( int ( row / 2 )) :
        khat_fard ( column )
        khat_zoj ( column )

else :
    for i in range ( int ( row / 2 )) :
        khat_fard ( column )
        khat_zoj ( column )
    khat_fard ( column )
