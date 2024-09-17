import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Importar dados (Certifique-se de analisar as datas. Considere definir a coluna do índice como 'date'.)
df = pd.read_csv('Page View Time\\fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Limpar os dados removendo os 2.5% superiores e inferiores
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Desenhar gráfico de linha
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(df.index, df['value'], color='b', linewidth=1)

    # Definir o título e os rótulos
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Salvar imagem e retornar a figura
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copiar e modificar dados para o gráfico de barras mensal
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Agrupar por ano e mês e calcular a média
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Desenhar gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))
    df_bar.plot(kind='bar', ax=ax)

    # Definir o título e os rótulos
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Salvar imagem e retornar a figura
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Preparar os dados para os gráficos de caixa
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Desenhar gráficos de caixa (Seaborn)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico de Caixa por Ano
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    
    # Gráfico de Caixa por Mês
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1],
                order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Salvar imagem e retornar a figura
    fig.savefig('box_plot.png')
    return fig
