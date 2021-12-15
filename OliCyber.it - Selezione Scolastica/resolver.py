# ESERCIZIO Data la seguente funzione --> Sottrazione

def f(a, b):
    if(b == 0) :
        return a
    if(b > 0):
        return f(a, b - 1) - 1
    return f(a, b + 1) + 1

#print(f(10,3))
# -----------------------------------------------------------------

# ESERCIZIO Considera le seguenti funzioni --> x(100) = 60

def x(n):
  if(n <= 0):
    return 0
  return 1+y(n-3)

def y(n):
  if(n <= 0):
    return 0
  return 2+x(n-2)

#print(x(100))
# -----------------------------------------------------------------

# ESERCIZIO Considera la seguente operazione: (17 | (x^31)) & 63 --> x = 6

def logical_function(x):
    return (17 | (x^31)) & 63

#print(logical_function(6)