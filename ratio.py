
def ratio_num(d_num, d_den, den):
    '''d_num is desired numerator, d_den is desired denominator, and den is known denominator.'''
    leftside = (d_num*den)
    rightside = d_den
    if rightside == 1:
        return leftside
    elif rightside != 1:
        return leftside/rightside
        
def ratio_den(d_num, d_den, num):
    '''d_num is desired numerator, d_den is desired denominator, and den is known numerator.'''
    leftside = (num*d_den)
    rightside = d_num
    if rightside == 1:
        return leftside
    elif rightside != 1:
        return leftside/rightside

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
    elif len(list) < 4:
        print('Error:\n\t List must be 4 items long. Variable must be in position 3 or 4.')
    elif len(list) > 4:
        print('Error:\n\t List is too short. Please add variable in position 3 or 4')