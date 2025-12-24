import pandas as pd
import os

def criar_kpis():
    diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
    projeto_raiz = os.path.dirname(diretorio_do_script)
    caminho_entrada = os.path.join(projeto_raiz, 'data', 'silver', 'vendas_limpas.csv')
    caminho_saida = os.path.join(projeto_raiz, 'data', 'gold', 'kpi_deposito.csv')
    
    os.makedirs(os.path.join(projeto_raiz, 'data', 'gold'), exist_ok=True)

    df = pd.read_csv(caminho_entrada)

    # Agrupamento por Produto e Marca (Foco do Depósito)
    kpi = df.groupby(['produto', 'marca']).agg({
        'quantidade': 'sum',
        'valor_total': 'sum'
    }).reset_index()

    kpi.to_csv(caminho_saida, index=False)
    print(f"✅ [AGGREGATE] KPIs de Produto/Marca gerados na Gold.")

if __name__ == "__main__":
    criar_kpis()