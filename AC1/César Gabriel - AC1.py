# Exercício 1

print("Para calcular as raízes da equação de segundo grau ax^2 + bx + c: \n")
a = float(input("insira o parâmetro a da equação: "))
b = float(input("insira o parâmetro b da equação: "))
c = float(input("insira o parâmetro c da equação: "))

x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)

print("A primeira raíz da equação é ", round(x1, 3))
print("A segunda raíz da equação é ", round(x2, 2))

# Exercício 2

ano = int(input("Informe o ano: "))
resto = ano % 4
print(ano and resto == 0)