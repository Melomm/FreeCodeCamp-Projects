import numpy as np

def calculate(input_list):
    # Verifica se a lista de entrada contém exatamente 9 elementos
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Converte a lista de entrada em uma matriz NumPy 3x3
    matrix = np.array(input_list).reshape(3, 3)
    
    # Cria o dicionário para armazenar os resultados
    calculations = {
        'mean': [
            # Calcula a média por colunas (axis=0), por linhas (axis=1) e para a matriz achatada
            np.mean(matrix, axis=0).tolist(),
            np.mean(matrix, axis=1).tolist(),
            np.mean(matrix).tolist()
        ],
        'variance': [
            # Calcula a variância por colunas, por linhas e para a matriz achatada
            np.var(matrix, axis=0).tolist(),
            np.var(matrix, axis=1).tolist(),
            np.var(matrix).tolist()
        ],
        'standard deviation': [
            # Calcula o desvio padrão por colunas, por linhas e para a matriz achatada
            np.std(matrix, axis=0).tolist(),
            np.std(matrix, axis=1).tolist(),
            np.std(matrix).tolist()
        ],
        'max': [
            # Calcula o valor máximo por colunas, por linhas e para a matriz achatada
            np.max(matrix, axis=0).tolist(),
            np.max(matrix, axis=1).tolist(),
            np.max(matrix).tolist()
        ],
        'min': [
            # Calcula o valor mínimo por colunas, por linhas e para a matriz achatada
            np.min(matrix, axis=0).tolist(),
            np.min(matrix, axis=1).tolist(),
            np.min(matrix).tolist()
        ],
        'sum': [
            # Calcula a soma por colunas, por linhas e para a matriz achatada
            np.sum(matrix, axis=0).tolist(),
            np.sum(matrix, axis=1).tolist(),
            np.sum(matrix).tolist()
        ]
    }

    # Retorna o dicionário com todos os cálculos
    return calculations
