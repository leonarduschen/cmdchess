def to_cartesian(algebraic):
    mapper = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8}

    hor = mapper[algebraic[0]]
    ver = int(algebraic[1])

    return (hor, ver)

def to_algebraic(cartesian):
    mapper = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}
    
    files = mapper[cartesian[0]]
    rank = str(cartesian[1])

    return files + rank