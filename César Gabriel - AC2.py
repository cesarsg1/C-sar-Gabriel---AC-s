# AC 2
# Exercício 1

def eq_seg_grau(a, b, c):
    return round((-b + (b**2 - 4*a*c)**0.5) / (2*a), 2), round((-b - (b**2 - 4*a*c)**0.5) / (2*a), 2)

print(eq_seg_grau(1, 12, -13))

def bissexto(ano):
    return ano and ano % 4 == 0

print(bissexto(1996))

# Exercício 2

def calcula_salario(valor_hora, num_horas):
    irpf = 0.215
    salario = valor_hora * num_horas
    return salario - (salario * irpf)

print(calcula_salario(50, 220))