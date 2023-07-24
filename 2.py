print (" 🧮 MULTIPLICATION TABLE 🧮 ")
print (" Please enter the lengths of multiplication table as input ")

def zarb ( column, row ) :
    hasel_zarb = [ row ]
    for i in range ( 1 , column + 1 ) :
        hasel_zarb.append ( i * row )
    return hasel_zarb

row = int ( input (" Please enter the number of rows in table : "))
column = int ( input (" Please enter the number of columns in table : "))

M_Table = []
first_row = ["X"]

for i in range (1, column + 1) :
    first_row.append (i)

M_Table.append ( first_row )

for i in range ( 1 , row + 1 ) :
    new_row = zarb ( column , i )
    M_Table.append ( new_row )

for line in M_Table :
    print ( line )