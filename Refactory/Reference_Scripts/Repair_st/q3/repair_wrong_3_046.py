def remove_extras ( lst ) :
    a = [ ]
    for i in lst :
        if ( i not in a ) :
            a += [ i ]
    return a
