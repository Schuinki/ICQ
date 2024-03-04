c1 = float(input('Digite o real do 1o:'))
c2 = float(input('Digite o real do 2o:'))
c5 = float(input('Digite o real do 3o:'))
c3 = float(input('Digite o imaginario do 1o:'))
c4 = float(input('Digite o imaginario do 2o:'))
c6 = float(input('Digite o imaginario do 3o:'))
complex1 = complex(c1, c3)
complex2 = complex(c2, c4)
complex3 = complex(c5, c6)
c = 0
print('Comutatividade:')
if(complex1 + complex2 == complex2 + complex1):
    print('Comutatividade da Soma OK')
    c = c + 1
if(complex1 * complex2 == complex2 * complex1):
    print('Comutatividade da Multiplicação OK')
    c = c + 1
print('Associatividade:')
if((complex1+complex2)+complex3 == complex1 + (complex2+complex3)):
    print('Associatividade da Soma OK')
    c = c + 1
if((complex1*complex2)*complex3 == complex1*(complex2*complex3)):
    print('Associatividade da Multiplicação OK')
    c = c + 1
if(complex1*(complex2+complex3) == complex1*complex2 + complex1*complex3):
    print('Distributividade OK')
    c = c + 1
if c == 5:
    print('Todas as propriedades foram verificadas pelo codigo')