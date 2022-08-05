#
 #   >>> fizbuzz(7)
 #   1
 #   fizz
 #   buzz
 #   fizz
 #   5
 #   fizzbuzz  
 #   7
#
def fizzbuzz(n):
    for i in range(1, n+1):
        resultado=''
        if i % 2: 
            resultado = "fizz"
        if i % 3:
            resultado += "buzz"
        if resultado=="":
            resultado = i
        print(resultado)