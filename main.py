__author__ = "Jorge Salgado A01636629, Fernando Muñoz Herrada A0"
__date__ = "October 15"
__version__ = "1.0"

## This program will have the next functions:
# 1) Read a .txt file to create a NDFA
# 2) from the same .txt file verify if the input is valid for that NDFA for this we have the next funtcions:
#   a) transition function -> return me where do i get from q0 with a for example
#   b) union -> return the union of two arrays WITHOUT duplicates
#   c) extended transition function -> main function that has the recursion®®

# This function will read the .txt and save all the values into the correct variables
# can change parameters

import sys
import re

# Global variables for the correct funcionality of the program
states = []
alphabet = []
initial_state = ""
final_states = []
transition_table = {}
string_to_check = ""
file = ""

def read_document(file):
    file = open(file, "r")
    var_globals = globals()

    var_globals['states'] = file.readline().replace("\n", "").split(",")
    var_globals['alphabet'] = file.readline().replace("\n", "").split(",")
    var_globals['initial_state'] = file.readline().replace("\n", "")
    var_globals['final_states'] = file.readline().replace("\n", "").split(",")

    for line in file:
        line = line.replace("\n", "")
        line = re.split(',|=>', line)

        if var_globals['transition_table'].get(line[0]) is None:
            var_globals['transition_table'][line[0]] = {}
            var_globals['transition_table'][line[0]][line[1]] = line[2:]
        else:
            var_globals['transition_table'][line[0]][line[1]] = line[2:]

    return 0


# This function will recive the values and create the dictonaries
# can change parameters
def create_NDFA():
    return 0


# This function will return the states where you can go from state with character
def transition_function(state, character):
    global transition_table
    return transition_table[state].get(character)


# This function will return the union of two arrays WITHOUT duplicates
def union(state1, state2):
    states = state1 + state2
    return list(dict.fromkeys(states))

def intersection(state1, state2):
    result = []
    for i in state1:
        if i in state2:
            result.append(i)
    return result


# This is the main function that has the recursion to verify if the input is valid
def extended_transition_function(state, word):
    #print(word)
    if len(word) == 0:
        #print(state)
        return state
    elif len(word) == 1:
        #print("word: ", word, "transition: ", transition_table[state].get(word))
        return transition_table[state].get(word)
    else:
        return_states = extended_transition_function(state, word[0:-1])
        char_verify = word[-1]
        #print("caracter a ver: ", char_verify)
        #print("return states ", return_states)

        final_states = []
        for state_temp in return_states:
            #print("state_temp: ", state_temp, "word: ", char_verify)
            #print("llamando a transición: ", transition_function(state_temp, char_verify))
            container = transition_function(state_temp, char_verify)
            if container is not None:
                final_states = union(final_states, container)

        #print("final states: ", final_states)
        return final_states


def main():
    global file, string_to_check
    file = sys.argv[1]
    string_to_check = sys.argv[2]
    #file = "test1.txt"
    #string_to_check = "abab"

    read_document(file)

    """print("states:", states)
    print("alphabet:", alphabet)
    print("initial_state:", initial_state)
    print("final_states:", final_states)
    print("transition_table:", transition_table) """

    #print("\nInicia debug \n")
    result = extended_transition_function(initial_state, string_to_check)
    #print("resultado: ", result)
    intersection_result = intersection(final_states, result)

    if len(result) == 0:
        print("\nLa cadena no es valida")
    elif len(intersection_result) > 0:
        print("\nLa cadena es valida")
    else:
        print("\nla cadena no es valida")




main()
