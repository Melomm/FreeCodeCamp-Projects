import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importar os dados
df = pd.read_csv('Medical Data\\medical_examination.csv')

# 2. Adicionar a coluna 'sobrepeso' e remover a coluna 'IMC' depois de usá-la
df['IMC'] = df['weight'] / ((df['height'] / 100) ** 2)
df['sobrepeso'] = df['IMC'].apply(lambda x: 1 if x > 25 else 0)  # 1 para sobrepeso, 0 caso contrário
df = df.drop(columns=['IMC'])  # Remover a coluna IMC após usá-la

# 3. Normalizar os dados de colesterol e glicose
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)  # 0 é bom, 1 é ruim
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)  # 0 é bom, 1 é ruim

# 4. Gerar o Gráfico Categórico na função draw_cat_plot
def draw_cat_plot():
    # 5. Criar o DataFrame para o gráfico categórico usando pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'sobrepeso'])
    
    # 6. Agrupar e reformular os dados para dividir por cardio e mostrar as contagens de cada variável
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7. Criar o gráfico categórico usando seaborn
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat).fig

    # 8. Salvar a figura
    fig.savefig('grafico_categorico.png')
    return fig

# 10. Gerar o Mapa de Calor na função draw_heat_map
def draw_heat_map():
    # 11. Limpar os dados
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]
    
    # 12. Calcular a matriz de correlação
    corr = df_heat.corr()

    # 13. Gerar uma máscara para o triângulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Configurar a figura do matplotlib
    fig, ax = plt.subplots(figsize=(12, 10))

    # 15. Plotar o mapa de calor
    sns.heatmap(corr, mask=mask, annot=True, fmt='.1f', cmap='coolwarm', square=True, linewidths=.5, ax=ax)

    # 16. Salvar a figura
    fig.savefig('mapa_de_calor.png')
    return fig

# Chamar as funções para gerar ambos os gráficos
if __name__ == "__main__":
    draw_cat_plot()  # Gerar o gráfico categórico
    draw_heat_map()  # Gerar o mapa de calor
