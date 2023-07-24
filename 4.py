print (" 🔺 KHAYAM PASKAL TRIANGLE 🔺 ")
print (" Please enter the number of this triangle's rows you want to be showen as an input ")

def khat ( qabli ) :
    before = qabli
    line = [ 1 ]

    for i in range ( len (before) - 1) :
        new = before [ i ] + before [ i+1 ]
        line.append ( new )

    line.append ( 1 )
    return line 

row = int ( input (" Please enter the number of rows : "))
triangle = []

if row >= 1 :
    first = [ 1 ]
    triangle.append ( first )

if row >= 2 :
    last = [ 1 , 1 ]
    triangle.append ( last )

if row >= 3 :
    for i in range ( row - 2 ) :
        new = khat ( last )
        triangle.append ( new )
        last = new

for line in triangle :
    print ( line )