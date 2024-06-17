#Ex7. O que é exibido pelas seguinte instruções (se executadas através de um script):
from unittest import case


v1 = [0]*4
i = 0
v1[i] = 7; i+=1; v1[i] = 14; v1[len(v1) - 1] = 15
print(v1[i]*v1[i+1] + v1[1])

codigo = {'A': 19, 'B': 20}
print(codigo['B'], codigo.get('C'), codigo.get('C', 21))

processos = {'ls': 192, 'grep': 321, 'init': 1}
print('ls' in processos, 321 in processos)
print((192 in processos)*2)
processos.update(ls=292, mkfs=19)
print(list(processos.items()))

txt = ''
nums = [10, 11]
if nums:
 print("Um")
 if not txt:
  print("Dois")
 txt = 'abc'
 nums = []
else:
 print("Três")
 txt = 'xey'
 nums[-1:] = [12]

txt = txt.replace('a', '').replace('e', '')
print("Quatro" if len(nums) else "Cinco")
print(txt if len(nums) == 0 else nums)

#Ex9. Converta as seguintes decisões if-else/match-case em match-case/if-else:
# a) i = int(input("Valor de i: "))
#if i == 10:
#print("Preparar operação")
#elif i == 5:
#print("Começar operação")
#elif i == 0:
#print("Missão crítica")
#else:
#print("Operação abortada")


print("Preparar operação")
print("Começar operação")
print("Missão crítica")
print("Operação abortada")

operacao = input("Valor de i: ")

match operacao:
 case '10':
  print("Preparar operação")
 case '5':
  print("Começar operação")
 case '0':
  print("Missão crítica")
 case _:
  print ("Operação abortada")


# b) nome = input("Nome? ")
#match nome:
#case 'Alberto' | 'Armando':
#print("Bom rapaz")
#case 'Arnaldo' | 'Augusto':
#print("Gente estranha...")
#case _:
#print("Desconheço...")

print("Bom rapaz")
print("Gente estranha...")
print ("Desconheço")

nome = input("Nome? ")

if nome == 'Alberto' or nome == 'Armando':
   print("Bom rapaz")
elif nome == 'Arnaldo' or nome == 'Augusto':
   print("Gente estranha...")
else:
   print("Desconheço")

# c) nums = ... deve ser um tuplo com três valores mas pode haver um erro...
#if len(nums) != 3 or not isinstance(nums, tuple):
#print("Conjunto inválido")
#elif nums[0] == 10:
#print(nums[1] + nums[2])
#elif nums[0] == 1:
#print(nums[1] * nums[2])
#else:
#print("Conjunto inválido")


nums = '!=3' | 'not isinstance (nums, tuple)'
#quaisquer conjunto de 3 valores.

match nums:
 case 'nums[0] == 10':
  print(nums[1] + nums [2])
 case 'nums[0] == 1':
  print(nums[1] * nums[2])
 case _:
  print("Conjunto inválido") 

#Ex10.Faça um programa para calcular o preço de venda final de um produto

preço = float(input("Digite o preço do produto: "))
IVA = float(input("Digite o valor da taxa IVA (em %): ")) # IVA 23% ou 13%
desconto = input("Digite o valor do desconto (em %): ") 

def preçofinal (preço, IVA, desconto = 0):
  valorIVA = preço * IVA / 100
  preçofinal = preço + valorIVA 

if 'desconto != 0':
  valorDesconto = preçofinal * desconto / 100
  pagarDesconto = preçofinal - valorDesconto
  print("O valor a pagar é: %.2f euros" % pagarDesconto)
else: 
 print("O valor do produto sem desconto é: %.2f euros ", preçofinal) 

preçofinal(preço, IVA, desconto)

