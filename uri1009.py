# -*- coding: utf-8 -*-
nome_funcionario = input()
salario_fixo = float(input())
total_vendas = float(input())

salario_total = float(salario_fixo + (total_vendas * 0.15))
print("TOTAL = R$ %0.2f" %salario_total)