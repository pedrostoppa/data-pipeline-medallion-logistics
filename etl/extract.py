import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def gerar_massa_mensal(mes=1, ano=2024):
    caminho_bronze = 'data/bronze/vendas_mensais.csv'
    os.makedirs('data/bronze', exist_ok=True)
    
    produtos = {
        'GÁS P13': ['Ultragaz', 'Consigaz', 'Liquigás'],
        'ÁGUA 20L': ['Lindoya', 'Bonafont', 'Cristal'],
        'VALVULA': ['Click', 'Vinigas']
    }
    canais = ['WhatsApp', 'Telefone', 'Aplicativo', 'Balcão']
    pagamentos = ['Dinheiro', 'Pix', 'Cartão Crédito', 'Cartão Débito']
    registros = 20000 
    
    data_inicial = datetime(ano, mes, 1)
    dados = []
    
    for i in range(registros):
        dia = np.random.randint(0, 28)
        data_venda = data_inicial + timedelta(days=dia)
        prod = np.random.choice(list(produtos.keys()))
        marca = np.random.choice(produtos[prod])
        preco = 110.0 if prod == 'GÁS P13' else 25.0 if prod == 'ÁGUA 20L' else 15.0
        
        dados.append({
            'data_venda': data_venda.strftime('%Y-%m-%d'),
            'id_venda': i + 1000,
            'tipo_cliente': np.random.choice(['pessoa_fisica', 'comercio'], p=[0.7, 0.3]),
            'produto': prod,
            'marca': marca,
            'quantidade': np.random.randint(1, 4),
            'preco_unitario': f"R$ {preco:.2f}".replace('.', ','), # Sujeira proposital
            'canal_venda': np.random.choice(canais),
            'forma_pagamento': np.random.choice(pagamentos),
            'cnpj': np.random.choice(['12.345.678/0001-99', None], p=[0.5, 0.5]) # Simula falta de CNPJ
        })

    df = pd.DataFrame(dados)
    df.to_csv(caminho_bronze, index=False)
    print(f"✅ [EXTRACT] 20k registros gerados em: {caminho_bronze}")

if __name__ == "__main__":
    gerar_massa_mensal()