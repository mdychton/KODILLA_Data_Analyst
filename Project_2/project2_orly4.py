a = 1
b = -2
c = -5

def equation(a,b,c):
  delta = b**2 - 4*a*c

  if delta < 0:
    return "Brak rozwiązań"

  elif delta == 0:
    x0 = -b / (2*a)
    return x0

  else:
    x1 = (-b - delta**(0.5)) / (2*a)
    x2 = (-b + delta**(0.5)) / (2*a)
    return x1,x2
  
print(equation(a,b,c))