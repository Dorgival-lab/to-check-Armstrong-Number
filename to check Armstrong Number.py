# Programa Python para determinar se o número é
# Número Armstrong ou não
  
# Função para calcular x elevado à potência y 
def power(x, y): 
    if y==0: 
        return 1
    if y%2==0: 
        return power(x, y/2)*power(x, y/2) 
    return x*power(x, y/2)*power(x, y/2) 
  
# Função para calcular a ordem do número 
def order(x): 
  
    # variável para armazenar o número 
    n = 0
    while (x!=0): 
        n = n+1
        x = x/10
    return n 
  
# Função para verificar se o número fornecido é
# Número Armstrong ou não 
def isArmstrong (x): 
    n = order(x) 
    temp = x 
    sum1 = 0
    while (temp!=0): 
        r = temp%10
        sum1 = sum1 + power(r, n) 
        temp = temp/10
  
    # Se a condição satisfizer 
    return (sum1 == x) 
  
  
# Driver Program 
x = 153
print(isArmstrong(x)) 
x = 1253
print(isArmstrong(x))