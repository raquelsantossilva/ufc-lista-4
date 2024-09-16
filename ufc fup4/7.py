salario = float(input(""))
parcela = float(input(""))
if parcela > (salario*20)/100:
    print("Emprestimo nao concedido")
else:
    print("Emprestimo concedido")
