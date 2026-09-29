import matplotlib.pyplot as plt

# 1. Lista com os dias e os valores
dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
vendas = [1200, 1450, 1100, 1800, 3200, 4100, 2300]

# 2. Monta o gráfico de barras
plt.bar(dias, vendas)

# 3. Adiciona textos explicativos
plt.title('Vendas da Semana')
plt.xlabel('Dia')
plt.ylabel('Vendas (R$)')

# 4. Exibe o gráfico
plt.show()