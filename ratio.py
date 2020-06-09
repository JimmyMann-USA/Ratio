
# Solves for the numerator to fit a desired ratio, with desired numerator, desired denominator, and current denominator.
def ratio_num(d_num, d_den, den):
    # Automates Cross Multiplying and Isolating Variable
    return (d_num * den)/d_den

# Solves for the denominator.
def ratio_den(d_num, d_den, num):
    # Automates Cross Multiplying and isolating variable
    return (d_den * num)/d_num

def ratio(list=[]):
    '''Cross-Multiplication Solver. Returns what you're solving for.
    List can only contain 4 values in this order:
    (1) desired ratio- numerator,
    (2) desired ratio- denominator,
    (3) Either: Numerator you're solving for (as string), or given numerator,
    (4) Either: Denominator you're solving for (as string), or given denominator.'''
    if len(list) == 4:
        if type(list[2]) != int:
            return ratio_num(list[0], list[1], list[3])
        elif (list[3]) != int:
            return ratio_den(list[0], list[1], list[2])
        else:
            print('Error:\n\t Variable not included or in wrong position.\n Variable only accepted in position 3 or 4')
    elif len(list) > 4:
        print('Error:\n\t List must be 4 items long. Variable must be in position 3 or 4.')
    elif len(list) < 4:
        print('Error:\n\t List is too short. Please add variable in position 3 or 4')

# r = [1, 4, 'x', 300]
# print(ratio(r))
