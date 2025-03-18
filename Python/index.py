dados = list()
ordem = list()
bairro = list()
quilometragem = list()
valores = list()

entrada_de_dados = input('Insira os dados aqui: ')
while entrada_de_dados:
    if entrada_de_dados.lower() == 'acabou':
        break
    dados.append(entrada_de_dados)
    entrada_de_dados = input('Insira os dados aqui: ')

for linha in dados:
    partes = linha.split()
    ordem.append(int(partes[0].split('°')[0]))
    bairro.append(' '.join(partes[1:-1]))
    km_str = partes[-1].replace(',', '.')
    if 'm' in km_str:
        quilometragem.append(float(km_str.replace('m', '')) / 1000)
    elif 'km' in km_str:
        quilometragem.append(float(km_str.replace('km', '')))
    else:
        quilometragem.append(float(km_str))

lista_final = list()
lista_final.append(ordem)
lista_final.append(bairro)
lista_final.append(quilometragem)

acumulador = 0
for km in quilometragem:
    if km <= 1.0:
        valor = 6
    elif km <= 2.2:
        valor = 7
    elif km <= 3.2:
        valor = 8
    elif km <= 4.0:
        valor = 9
    elif km <= 4.8:
        valor = 10
    elif km <= 5.6:
        valor = 11
    elif km <= 6.4:
        valor = 12
    elif km <= 7.2:
        valor = 13
    elif km <= 8.0:
        valor = 14
    elif km <= 8.8:
        valor = 15
    elif km <= 9.6:
        valor = 16
    elif km <= 10.4:
        valor = 17
    elif km <= 11.2:
        valor = 18
    elif km <= 12.0:
        valor = 19
    elif km <= 13.0:
        valor = 20
    elif km <= 15.0:
        valor = 25

    valores.append(valor)
    acumulador += valor

print(f"{'Ordem':<5} {'Bairro':<5}  {'Valor':<5}")
for i in range(len(ordem)):
    print(f"{ordem[i]}° - {bairro[i]} - R${valores[i]}")

print(f'Total: R${acumulador}')

1 contra 2.5km
2 jardim 2.1km
3 bacuri 4.5km
1 contra 2.5km
2 jardim 2.1km
3 bacuri 4.5km
1 contra 2.5km
2 jardim 2.1km
3 bacuri 4.5km
1 contra 2.5km
2 jardim 2.1km
3 bacuri 4.5km
1 contra 2.5km
2 jardim 2.1km
3 bacuri 4.5km
1 contra 2.5km
2 jardim 2.1km
3 bacuri 4.5km
1 contra 2.5km
2 jardim 2.1km
3 bacuri 4.5km
1 contra 2.5km
2 jardim 2.1km
3 bacuri 4.5km
