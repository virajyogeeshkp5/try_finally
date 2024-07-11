# try & finally
try:
    str = 'rahul'
    n = len(str)-1
    while n>0:
        print(str[n])
        n=n-1
finally:
    print("hello")