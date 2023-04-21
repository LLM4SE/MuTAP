def search ( x , seq ) :
    ' Takes in a value x and a sorted sequence seq, and returns the\n    position that x should go to such that the sequence remains sorted '
    seq = tuple ( seq )
    if ( seq == ( ) ) :
        return 0
    elif ( x > seq [ ( len ( seq ) - 1 ) ] ) :
        return len ( seq )
    else :
        i = 0
        while ( i <= ( len ( seq ) - 1 ) ) :
            if ( x <= seq [ i ] ) :
                return i
            elif ( x > seq [ i ] ) :
                i += 1
