import random
import string

class atoom_property :
    def __init__(self, position ):
        self.position = position

    def selecting_random_atom (self , atoms  ): # this method selecting the random atom from the list that we provide to it (this list is defin in the main.py file mr fozveh )
        self.atoms = atoms
        selected_atom = random.choices( atoms[0] , weights =atoms[1] )[0] # randomly select with weight of the atom ( for example fe =4 )
        self.position.append ( selected_atom)

        return (self.position)



        # self.array.append()






    def add_random_value(self):
        value = random.choice([1, 2, 3])
        self.array.append(value)



position_input = [0.00001, 0.00001 , 0.00001]
elements = [[ 'Al' , 'Fe' , 'Ni' , 'Cr' , 'Co'] , [ 4 , 1 , 1 , 1 , 1 ] ]



postinon_from_class  = atoom_property (  position_input )
print("Initial array from calss : ",  postinon_from_class.position )



selected_elm = postinon_from_class.selecting_random_atom(elements)
print("Array after adding random name:", selected_elm )





# atom_array.add_random_value()
# print("Array after adding random value:", atom_array.array)