import random
import string
import numpy as np
class atoom_property :
    def __init__(self, position   ):
        self.position = position


    def selecting_random_atom (self , atoms  , edited_atoms ): # this method selecting the random atom from the list that we provide to it (this list is defin in the main.py file mr fozveh )
        self.atoms = atoms
        self.edited_atoms = edited_atoms
        print('this is atoms[1]' , atoms[1])
        selected_atom = random.choices( atoms[0] , weights =edited_atoms[1] )[0] # randomly select with weight of the atom ( for example fe =4 )
        self.position.append ( selected_atom )
        with_atom_index = edited_atoms[0].index(selected_atom) # find with atom is selected randomly
        print('this is the index of the selected atom in the atoms 0', with_atom_index)
        edited_atoms[1][with_atom_index] -= 1
        print('this is editedeatoms[1]' , edited_atoms[1] )
        print('this is atoms local ' , atoms[1])
        # adding the lable :) do it in the same method :)  # i found the amazing way to adding tha lavle :) this is alioooo :)
        # az ravesh menha estefadeh mikonim :)
        reduce = np.array(atoms[1]) - np.array(edited_atoms[1])

        print( 'this is alio ' , reduce ) #adding lable
        for i in  reduce  :
            if ( i > 0 ) :
                iindex= np.where( reduce == i )[0][0]
                print(iindex)
                self.position.append( str(f'{atoms[0][iindex]}' f'{i}')  )

        return (self.position)














position_input = [0.00001, 0.00001 , 0.00001]
elements = [[ 'Al' , 'Fe' , 'Ni' , 'Cr' , 'Co'] , [ 8 , 2 , 2 , 2 , 2 ] ]



postinon_from_class  = atoom_property (  position_input  )
print("Initial array from calss : ",  postinon_from_class.position )
alioo = [[ 'Al' , 'Fe' , 'Ni' , 'Cr' , 'Co'] , [6,2,2,2,2]]

selected_elm = postinon_from_class.selecting_random_atom(elements , alioo )
print("Array after adding random name:", selected_elm )





# atom_array.add_random_value()
# print("Array after adding random value:", atom_array.array)