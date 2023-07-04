import numpy as np

input_fozveh_list = np.loadtxt ( 'input.txt'  )
lent = len(input_fozveh_list) #104
elements = [[ 'al' , 'Fe' , 'Ni' , 'Cr' , 'Co'] , [ 4 , 1 , 1 , 1 , 1 ] ]
# vaznesh = [ 4 , 1 , 1 , 1 , 1 ]

if (lent > 8 ) :
    zarib = lent / 8
    elements[1] = [ zarib*4 , zarib , zarib , zarib , zarib ]









# print(  input_fozveh_list[0] )
