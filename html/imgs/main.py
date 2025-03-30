import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Carregando dataset com pandas
games_df = pd.read_csv('data/games_mental_health.csv').drop(columns=['ID'])
print(games_df)

# Exibindo as primeiras linhas
print("Primeiras linhas do DataFrame:")
print(games_df.head())

# Exibindo as informações gerais
print("Informações do DataFrame:")
print(games_df.info())

# Exibindo as estatísticas descritivas
print("Estatísticas Descritivas do DataFrame:")
print(games_df.describe())

# Verificando a quantidade de dados faltantes ou inconstantes por coluna
print("Quantidade de dados faltantes por coluna:")
print(games_df.isnull().sum())

# Verificando o total de dados faltantes ou inconstantes no DataFrame
print("\nTotal de dados faltantes no DataFrame:")
print(games_df.isnull().sum().sum())

# Verificar a inconsistência de dados
print("\nQuantidade dados inconsistentes:")
print(games_df.duplicated().sum())


# Convertendo a coluna 'Horas_jogando_por_semana' para numérico
games_df['Horas_jogando_por_semana_raw'] = games_df['Horas_jogando_por_semana']
games_df['Horas_jogando_por_semana'] = games_df['Horas_jogando_por_semana'].round().astype(int)

# Ordenando os dados por idade e horas jogadas por semana
games_df = games_df.sort_values(by=['Horas_jogando_por_semana'])

# Histograma da distribuição de tempo jogando por semana
plt.figure(figsize=(12, 6))
sns.histplot(games_df['Horas_jogando_por_semana'], bins=20, kde=True, color='skyblue', edgecolor='black')
plt.title('Distribuição de Tempo Jogando por Semana', fontsize=14)
plt.xlabel('Horas Jogando por Semana', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.savefig('graphs/histograma_horas_jogando.png', dpi=300, bbox_inches='tight')
plt.show()

# Boxplot comparando níveis de estresse entre gêneros
plt.figure(figsize=(12, 6))
sns.boxplot(x='Genero', y='Nivel_estresse', data=games_df, palette='Set2')
plt.title('Distribuição de Estresse por Gênero', fontsize=14)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Nível de Estresse', fontsize=12)
plt.savefig('graphs/boxplot_estresse_genero.png', dpi=300, bbox_inches='tight')
plt.show()

# Gráfico de dispersão (scatter plot) entre tempo jogando e estresse com linha de tendência
plt.figure(figsize=(12, 6))
sns.scatterplot(x='Horas_jogando_por_semana', y='Nivel_estresse', data=games_df, color='black', alpha=0.8)
plt.title('Relação entre Tempo Jogando por Semana e Nível de Estresse', fontsize=14)
plt.xlabel('Horas Jogando por Semana', fontsize=12)
plt.ylabel('Nível de Estresse', fontsize=12)

# Calculando a linha de tendência (regressão linear)
x = games_df['Horas_jogando_por_semana']
y = games_df['Nivel_estresse']
a, b = np.polyfit(x, y, 1)

# gerar o coeficiente de correlacao de Pearson
x_raw = games_df['Horas_jogando_por_semana_raw']
correlation = np.corrcoef(x_raw, y)[0, 1]
print(f'Coeficiente de Correlação de Pearson: {correlation:.2f}')

# Plotando a linha de tendência
plt.plot(x, a * x + b, color='red', label='Linha de Tendência')
plt.legend()
plt.savefig('graphs/scatter_plot_estresse.png', dpi=300, bbox_inches='tight')
plt.show()

# Vamos analizar Estresse por Gênero
estresse_genero = games_df.groupby(['Genero', 'Idade'])['Nivel_estresse'].mean().unstack()
_df = games_df.copy()

# Calcular média, mediana, moda, desvio padrão e variância para colunas numéricas
# Printar a faixa de idade e horas jogadas por semana ordenadas
# ordenar as idades e horas jogadas por semana
# printar os dados
idades = (_df['Idade'].unique())
idades.sort()
media_idade = _df['Idade'].mean()
mediana_idade = _df['Idade'].median()
moda_idade = _df['Idade'].mode()[0]
desvio_padrao_idade = _df['Idade'].std()
variancia_idade = _df['Idade'].var()

print("Faixa de Idade:")
print(f"    Valores Analisados: {idades}")
print(f"    Média: {media_idade:.2f}")
print(f"    Mediana: {mediana_idade:.2f}")
print(f"    Moda: {moda_idade:.2f}")
print(f"    Desvio Padrão: {desvio_padrao_idade:.2f}")
print(f"    Variância: {variancia_idade:.2f}")


horas = (_df['Horas_jogando_por_semana'].unique())
horas.sort()
media_horas = _df['Horas_jogando_por_semana'].mean()
mediana_horas = _df['Horas_jogando_por_semana'].median()
moda_horas = _df['Horas_jogando_por_semana'].mode()[0]
desvio_padrao_horas = _df['Horas_jogando_por_semana'].std()
variancia_horas = _df['Horas_jogando_por_semana'].var()

print("Faixa de Horas Jogadas por Semana:")
print(f"    Valores Analisados: {horas}")
print(f"    Média: {media_horas:.2f}")
print(f"    Mediana: {mediana_horas:.2f}")
print(f"    Moda: {moda_horas:.2f}")
print(f"    Desvio Padrão: {desvio_padrao_horas:.2f}")
print(f"    Variância: {variancia_horas:.2f}")


estresse = (_df['Nivel_estresse'].unique())
estresse.sort()
media_estresse = _df['Nivel_estresse'].mean()
mediana_estresse = _df['Nivel_estresse'].median()
moda_estresse = _df['Nivel_estresse'].mode()[0]
desvio_padrao_estresse = _df['Nivel_estresse'].std()
variancia_estresse = _df['Nivel_estresse'].var()

print("Faixa de Estresse:")
print(f"    Valores Analisados: {estresse}")
print(f"    Média: {media_estresse:.2f}")
print(f"    Mediana: {mediana_estresse:.2f}")
print(f"    Moda: {moda_estresse:.2f}")
print(f"    Desvio Padrão: {desvio_padrao_estresse:.2f}")
print(f"    Variância: {variancia_estresse:.2f}")


# Vamos quebrar horas jogadas em intervalos de 2 horas
_df['Horas_jogando_por_semana'] = pd.cut(
    _df['Horas_jogando_por_semana'],
    bins=range(0, 27, 2),
    labels=[f"{i}-{i+2}" for i in range(0, 26, 2)]
)

# Vamos quebrar idade em intervalos de 5 anos
_df['Idade'] = pd.cut(
    _df['Idade'],
    bins=range(10, 51, 5),
    labels=[f"{i}-{i+5}" for i in range(10, 50, 5)]
)

# Tabela de Distribuição de Nivel_estresse por Gênero
idade_genero = _df.groupby(['Nivel_estresse', 'Genero']).size().unstack()
print(idade_genero.head(80))
# Heatmap de Distribuição de Nivel_estresse por Gênero
plt.figure(figsize=(12, 6))
sns.heatmap(
    idade_genero,
    cmap='YlOrRd',
    annot=True,  # Mostrar valores nas células
    linewidths=0.5,
    cbar_kws={'label': 'Contagem'}
)
plt.title('Distribuição de Nivel_estresse por Gênero', fontsize=14)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Nivel de Estresse', fontsize=12)
plt.savefig('graphs/heatmap_nivel_estresse_genero.png', dpi=300, bbox_inches='tight')
plt.show()

# Tabela de Distribuição de Idade por Gênero sem o Estresse
idade_genero = _df.groupby(['Idade', 'Genero']).size().unstack()
print(idade_genero.head(80))
# Heatmap de Distribuição de Idade por Gênero sem o Estresse
plt.figure(figsize=(12, 6))
sns.heatmap(
    idade_genero,
    cmap='YlOrRd',
    annot=True,  # Mostrar valores nas células
    linewidths=0.5,
    cbar_kws={'label': 'Contagem'}
)
plt.title('Distribuição de Idade por Gênero', fontsize=14)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Faixa de Idade', fontsize=12)
plt.savefig('graphs/heatmap_idade_genero.png', dpi=300, bbox_inches='tight')
plt.show()

# Tabela de Distribuição de Horas Jogadas por Semana por Gênero com a média de horas jogadas
horas_idade_genero = _df.groupby(['Genero'])['Horas_jogando_por_semana_raw'].mean()
print(horas_idade_genero.head(80))
# BarPlot de Distribuição de Horas Jogadas por Semana por Gênero com a média de horas jogadas
plt.figure(figsize=(12, 6))
sns.barplot(x=horas_idade_genero.index, y=horas_idade_genero.values, palette='Set2')
plt.title('Média de Horas Jogadas por Semana por Gênero', fontsize=14)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Média de Horas Jogadas', fontsize=12)
plt.savefig('graphs/barplot_horas_idade_genero.png', dpi=300, bbox_inches='tight')
plt.show()


# Tabela de Distribuição de Horas Jogadas por Semana por Gênero e Idade com a média de horas jogadas
horas_idade_genero = _df.groupby(['Idade', 'Genero'])['Horas_jogando_por_semana_raw'].mean().unstack()
print(horas_idade_genero.head(80))
# Heatmap de Distribuição de Horas Jogadas por Semana por Gênero e Idade com a média de horas jogadas
plt.figure(figsize=(12, 6))
sns.heatmap(
    horas_idade_genero,
    cmap='YlOrRd',
    annot=True,  # Mostrar valores nas células
    linewidths=0.5,
    cbar_kws={'label': 'Média de Horas Jogadas'}
)
plt.title('Média de Horas Jogadas por Semana por Gênero e Idade', fontsize=14)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Faixa de Idade', fontsize=12)
plt.savefig('graphs/heatmap_horas_idade_genero.png', dpi=300, bbox_inches='tight')
plt.show()

# Tabela de Nivel_estresse por Gênero
estresse_genero = _df.groupby(['Genero'])['Nivel_estresse'].mean()
print(estresse_genero.head(80))
# BarPlot de Nivel_estresse por Gênero
plt.figure(figsize=(12, 6))
sns.barplot(x=estresse_genero.index, y=estresse_genero.values, palette='Set2')
plt.title('Nível de Estresse por Gênero', fontsize=14)
plt.xlabel('Gênero', fontsize=12)
plt.ylabel('Nível de Estresse', fontsize=12)
plt.savefig('graphs/barplot_estresse_genero.png', dpi=300, bbox_inches='tight')
plt.show()

# Tabela de Nivel_estresse por Horas Jogadas por Semana
estresse_genero = _df.groupby(['Horas_jogando_por_semana', 'Genero'])['Nivel_estresse'].mean().unstack()
print(estresse_genero.head(80))
# Lineplot de Nivel_estresse por Horas Jogadas por Semana uma linha para cada gênero
plt.figure(figsize=(12, 6))
sns.lineplot(data=estresse_genero, palette='Set2')
plt.title('Nível de Estresse por Horas Jogadas por Semana', fontsize=14)
plt.xlabel('Horas Jogadas por Semana', fontsize=12)
plt.ylabel('Nível de Estresse', fontsize=12)
plt.legend(title='Gênero')
plt.savefig('graphs/lineplot_estresse_horas.png', dpi=300, bbox_inches='tight')
plt.show()

# Tabela de Nivel_estresse por Gênero e Horas Jogadas por Semana
estresse_genero = _df.groupby(['Horas_jogando_por_semana', 'Genero'])['Nivel_estresse'].mean().unstack()
print(estresse_genero.head(80))
# heatmap de Nivel_estresse por Gênero e Horas Jogadas por Semana
plt.figure(figsize=(12, 6))
sns.heatmap(
    estresse_genero,
    cmap='YlOrRd',
    annot=True,  # Mostrar valores nas células
    linewidths=0.5,
    cbar_kws={'label': 'Nível de Estresse'}
)
plt.title('Nível de Estresse por Gênero e Horas Jogadas por Semana', fontsize=14)
plt.ylabel('Horas Jogadas por Semana', fontsize=12)
plt.xlabel('Gênero', fontsize=12)
plt.savefig('graphs/heatmap_estresse_genero_horas.png', dpi=300, bbox_inches='tight')
plt.show()

# Tabela de Nivel_estresse por Gênero e Idade
idade_genero = _df.groupby(['Idade', 'Genero'])['Nivel_estresse'].mean().unstack()
print(idade_genero.head(80))
# Heatmap de Nivel_estresse por Gênero e Idade
plt.figure(figsize=(12, 6))
sns.heatmap(
    idade_genero,
    cmap='YlOrRd',
    annot=True,  # Mostrar valores nas células
    linewidths=0.5,
    cbar_kws={'label': 'Nível de Estresse'}
)
plt.title('Nível de Estresse por Gênero e Idade', fontsize=14)
plt.ylabel('Idade', fontsize=12)
plt.xlabel('Gênero', fontsize=12)
plt.savefig('graphs/heatmap_estresse_genero_idade.png', dpi=300, bbox_inches='tight')
plt.show()

# Dados já agregados (estresse_horas)
estresse_horas = _df.groupby(['Genero', 'Idade', 'Horas_jogando_por_semana'])['Nivel_estresse'].mean().unstack()
print(estresse_horas.head(80))

# Função para plotar heatmap
def plot_heatmap(data, title, cmap='YlOrRd'):
    plt.figure(figsize=(12, 6))
    sns.heatmap(
        data,
        cmap=cmap,
        annot=True,  # Mostrar valores nas células
        linewidths=0.5,
        cbar_kws={'label': 'Nível de Estresse'}
    )
    plt.title(title, fontsize=14)
    plt.xlabel('Horas Jogadas por Semana', fontsize=12)
    plt.ylabel('Faixa de Idade', fontsize=12)
    plt.savefig(f'graphs/heatmap_{title}.png', dpi=300, bbox_inches='tight')
    plt.show()

# Pegar os gêneros únicos
generos = estresse_horas.index.get_level_values('Genero').unique()

# Gerar heatmap para cada gênero
for genero in generos:
    dados_genero = estresse_horas.loc[genero]
    plot_heatmap(
        dados_genero,
        title=f'Relação entre Horas Jogadas e Estresse ({genero})',
        cmap='coolwarm' 
    )

# Gerar um histograma para cada gênero da distribuição de horas jogadas por semana
for genero in generos:
    dados_genero = _df[_df['Genero'] == genero]
    plt.figure(figsize=(12, 6))
    sns.histplot(dados_genero['Horas_jogando_por_semana'], bins=20, kde=True)
    plt.title(f'Distribuição de Horas Jogadas por Semana ({genero})', fontsize=14)
    plt.xlabel('Horas Jogadas por Semana', fontsize=12)
    plt.ylabel('Frequência', fontsize=12)
    plt.savefig(f'graphs/histograma_horas_jogando_{genero}.png', dpi=300, bbox_inches='tight')
    plt.show()

# Gerar um boxplot para cada gênero da distribuição de estresse
for genero in generos:
    dados_genero = _df[_df['Genero'] == genero]
    plt.figure(figsize=(12, 6))
    sns.boxplot(y='Nivel_estresse', x='Horas_jogando_por_semana', data=dados_genero, palette='Set2')
    plt.title(f'Distribuição de Estresse por Horas Jogadas ({genero})', fontsize=14)
    plt.xlabel('Horas Jogadas por Semana', fontsize=12)
    plt.ylabel('Nível de Estresse', fontsize=12)
    plt.savefig(f'graphs/boxplot_estresse_horas_{genero}.png', dpi=300, bbox_inches='tight')
    plt.show()

# Gerar um gráfico de dispersão para cada gênero da relação entre horas jogadas e estresse
# Adicionando linha de tendência
for genero in generos:
    dados_genero = _df[_df['Genero'] == genero]
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x='Horas_jogando_por_semana', y='Nivel_estresse', data=dados_genero, alpha=0.7)
    plt.title(f'Relação entre Horas Jogadas e Estresse ({genero}) com Linha de Tendência', fontsize=14)
    plt.xlabel('Horas Jogadas por Semana', fontsize=12)
    plt.ylabel('Nível de Estresse', fontsize=12)

    # Calculando a linha de tendência (regressão linear)
    x = dados_genero['Horas_jogando_por_semana']
    y = dados_genero['Nivel_estresse']
    a, b = np.polyfit(x.cat.codes, y, 1)  # a é o coeficiente angular e b é o coeficiente linear

    # gerar o coeficiente de correlacao de Pearson
    x_raw = dados_genero['Horas_jogando_por_semana_raw']
    correlation = np.corrcoef(x_raw, y)[0, 1]
    print(f'Coeficiente de Correlação de Pearson: {correlation:.2f}')

    # Plotando a linha de tendência
    plt.plot(x.cat.codes, a*x.cat.codes + b, color='red', label='Linha de Tendência')
    
    plt.legend()
    plt.savefig(f'graphs/scatter_plot_estresse_horas_{genero}.png', dpi=300, bbox_inches='tight')
    plt.show()