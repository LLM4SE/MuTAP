def search ( x , seq ) :
    if ( not seq ) :
        return len ( seq )
    elif ( ( seq [ 0 ] >= x ) or ( seq == ( ) ) or ( seq == [ ] ) ) :
        return 0
    else :
        for i in range ( ( len ( seq ) - 1 ) ) :
            if ( ( seq [ i ] < x ) and ( seq [ ( i + 1 ) ] >= x ) ) :
                return ( i + 1 )
                break
        return len ( seq )
