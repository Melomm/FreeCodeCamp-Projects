Este repositório possui os projetos de análise que fiz para o curso de Análise de Dados com Python da freeCodeCamp. Cada um dos cinco projetos e seus respectivos arquivos, incluindo datasets em CSV, scripts Python e figuras produzidas, estão descritos abaixo.

**1. Calculadora de Média, Variância e Desvio Padrão**

* Objetivo: Criar uma função chamada `calculate()` no arquivo `mean_var_std.py` que utiliza o Numpy para exibir a média, variância, desvio padrão, valor máximo, mínimo e a soma das linhas, colunas e elementos de uma matriz 3 x 3.
* Script Python: `mean_var_std.py`

**2. Analisador de Dados Demográficos**

* Objetivo: Dado um dataset de dados demográficos extraídos do banco de dados do Censo de 1994, analisar os dados demográficos utilizando Pandas.
* Script Python: `demographic_data_analyzer.py`

**3. Visualizador de Dados Médicos**

* Objetivo: Visualizar e fazer cálculos a partir de dados de exames médicos utilizando matplotlib, seaborn e pandas. Os valores do dataset foram coletados durante exames médicos, e esses dados foram usados para explorar a relação entre doenças cardíacas, medidas corporais, marcadores sanguíneos e escolhas de estilo de vida.
* Script Python: `medical_data_visualizer.py`
* Gráfico de barras categóricas (grafico_categorico.png): Um gráfico de barras comparando as características categóricas entre pacientes com valores de 'cardio' de 0 (ausência de doença cardiovascular) e 1 (presença de doença cardiovascular).  
<img src="Medical Data\Graficos\grafico_categorico.png" alt="Categorico" />

* Mapa de calor de correlação (mapa_de_calor.png): Uma matriz triangular que utiliza cores para visualizar a correlação entre variáveis de dados médicos.  
<img src="Medical Data\Graficos\mapa_de_calor.png" alt="Mapa de Calor" />

**4. Visualizador de Séries Temporais de Visualizações de Página**

* Objetivo: Visualizar dados de séries temporais utilizando um gráfico de linha, gráfico de barras e gráficos de caixa. Este projeto utiliza Pandas, Matplotlib e Seaborn para visualizar um dataset contendo o número de visualizações de página por dia no fórum da freeCodeCamp.org, de 09 de maio de 2016 a 03 de dezembro de 2019. As visualizações de dados ajudam a entender os padrões de visitas e identificar o crescimento anual e mensal.
* Script Python: `time_series_visualizer.py`
* Gráfico de linha (line_plot.png): Visualizações diárias de página do fórum freeCodeCamp de maio de 2016 a dezembro de 2019.  
<img src="Page View Time\Graficos\line_plot.png" alt="Line Plot" />

* Gráfico de barras (bar_plot.png): Visualizações médias de página por mês, agrupadas pelos anos de 2016 a 2019.  
<img src="Page View Time\Graficos\bar_plot.png" alt="Bar Plot" />

* Gráfico de caixa (box_plot.png): Visualizações de página por ano para visualizar a tendência (esquerda) e visualizações de página por mês para visualizar a sazonalidade (direita).  
<img src="Page View Time\Graficos\box_plot.png" alt="Box Plot" />

**5. Preditor do Nível do Mar**

* Objetivo: Analisar um dataset de mudanças no nível médio global do mar desde 1880 e usar os dados para prever a mudança do nível do mar até o ano de 2050.
* Script Python: `sea_level_predictor.py`
* Gráfico de dispersão com linha de regressão (sea_level_plot.png): Plota os valores do nível do mar de 1880 a 2013, incluindo uma linha vermelha de melhor ajuste que prevê o nível do mar até o ano de 2050. Uma linha de regressão rosa prevê o nível futuro do mar até 2050, mas considerando apenas os dados dos anos 2000 a 2013.  
<img src="Sea Level\Graficos\sea_level_plot.png" alt="Sea Level Plot" />