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
def read_document():
    return 0


# This function will recive the values and create the dictonaries
# can change parameters
def create_NDFA():
    return 0


# This function will return the states where you can go from state with character
def transition_function(state, character):
    return 0


# This function will return the union of two arrays WITHOUT duplicates
def union(state1, state2):
    return 0


# This is the main function that has the recursion to verify if the input is valid
def extended_transition_function(state, word):
    return 0


def main():
    print("hola")
    print(secondsToText(3632971.323))

def secondsToText(secs):
    months = secs//2592000
    days = (secs - months*2592000) // 86400
    #days = (secs - months * 2592000)//86400
    hours = (secs - months*2592000 - days*86400)//3600
    minutes = (secs - days*86400 - hours*3600)//60
    seconds = secs - days*86400 - hours*3600 - minutes*60

    result = ("{} months, ".format(months) if months else "") + \
             ("{} days, ".format(days) if days else "") + \
            ("{} hours, ".format(hours) if hours else "") + \
            ("{} minutes, ".format(minutes) if minutes else "") + \
            ("{} seconds, ".format(seconds) if seconds else "")
    return result


main()
print(60*60*24*30)