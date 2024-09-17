import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Carregar o conjunto de dados
    file_path = 'Sea Level\\epa-sea-level.csv'
    sea_level_data = pd.read_csv(file_path)

    # Criar gráfico de dispersão
    plt.scatter(sea_level_data['Year'], sea_level_data['CSIRO Adjusted Sea Level'])

    # Criar a primeira linha de melhor ajuste usando todos os dados
    slope_all, intercept_all, r_value, p_value, std_err = linregress(sea_level_data['Year'], sea_level_data['CSIRO Adjusted Sea Level'])
    years_extended_all = pd.Series(range(1880, 2051))
    plt.plot(years_extended_all, intercept_all + slope_all * years_extended_all, label='Best Fit Line 1880-2050', color='red')

    # Criar a segunda linha de melhor ajuste usando dados a partir de 2000
    recent_data = sea_level_data[sea_level_data['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_extended_recent = pd.Series(range(2000, 2051))
    plt.plot(years_extended_recent, intercept_recent + slope_recent * years_extended_recent, label='Best Fit Line 2000-2050', color='green')

    # Adicionar rótulos e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Salvar gráfico e retornar dados para testes
    plt.savefig('sea_level_plot.png')
    return plt.gca()

# Chamar a função para executar o gráfico
draw_plot()
