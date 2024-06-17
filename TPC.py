#Ex10.Faça um programa para calcular o preço de venda final de um produto

preço = float(input("Digite o preço do produto: "))
IVA = float(input("Digite o valor da taxa IVA (em %): ")) # IVA 23% ou 13%
desconto = float(input("Digite o valor do desconto (em %): ")) 

def preçofinal (preço, IVA, desconto = 0):
  valorIVA = preço * IVA / 100
  preçofinal = preço + valorIVA 

  if desconto != 0:
    valorDesconto = preçofinal * desconto / 100
    pagarDesconto = preçofinal - valorDesconto
    return pagarDesconto
    print("O valor a pagar é: %.2f euros" % pagarDesconto)
  else: 
    return preçofinal
    print("O valor do produto sem desconto é: %.2f euros" % preçofinal) 

valor_a_pagar = preçofinal (preço, IVA, desconto)
print("O valor a pagar é: %.2f euros" % valor_a_pagar)

