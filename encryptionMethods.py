#!/usr/bin/env python

# Vigenere Cipher
a = dict({'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9,
 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18,
 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25})

letters = list(a.keys())
values  = list(a.values())

def shift(letters,n):
    '''shift of list x by x + n'''
    return( letters[n:] + letters[:n] )


def encryptVigenere(message,keycode):
    '''Assumes keycode shorter than message'''
    # make message and keycode same length
    n = len(message)
    m = len(keycode)
    r = n % m

    totalcode = keycode
    for i in range( int( n / m ) - 1 ):
        totalcode += totalcode

    totalcode += keycode[:r]

    cipher = list(message)
    for i in range(len(message)):
        newletters = shift(letters,a[totalcode[i]])
        newvalues  = shift(values, a[totalcode[i]])
        cipher[i] = newletters[ a[ message [i] ] ]

    return(cipher)



def decryptVigenere(cipher,keycode):
    '''decrypts ciphers via reversed method'''
    n = len(cipher)
    m = len(keycode)
    r = n % m

    totalcode = keycode
    for i in range( int( n / m ) - 1 ):
        totalcode += totalcode

    totalcode += keycode[:r]

    message = cipher
    for i in range(len(message)):
        newletters = shift(letters,a[totalcode[i]])
        newvalues  = shift(values, a[totalcode[i]])
        message[i] = letters[ newletters.index( cipher[i] ) ]

    return(cipher)


## __main__
cipher = encryptVigenere("wikihowisthebest","lime")
print(cipher)

message = ''.join( decryptVigenere(cipher,"lime") )
print(message)