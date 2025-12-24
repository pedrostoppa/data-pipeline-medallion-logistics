import pandas as pd
import numpy as np
import os

def limpar_dados():
    diretorio_do_script = os.path.dirname(os.path.abspath(__file__))
    projeto_raiz = os.path.dirname(diretorio_do_script)
    caminho_entrada = os.path.join(projeto_raiz, 'data', 'bronze', 'vendas_mensais.csv')
    caminho_saida = os.path.join(projeto_raiz, 'data', 'silver', 'vendas_limpas.csv')
    
    os.makedirs(os.path.join(projeto_raiz, 'data', 'silver'), exist_ok=True)

    try:
        df = pd.read_csv(caminho_entrada)

        # Tratamento de Preço
        df['preco_unitario'] = df['preco_unitario'].str.replace('R$ ', '', regex=False).str.replace(',', '.')
        df['preco_unitario'] = df['preco_unitario'].astype(float)
        
        # Cálculo de Faturamento
        df['valor_total'] = df['preco_unitario'] * df['quantidade']
        
        # Tratamento de Datas e IDs
        df['data_venda'] = pd.to_datetime(df['data_venda'])
        df['id_venda'] = df['id_venda'].astype(int)

        # Regra de Negócio: Alerta de CNPJ faltante para Comércio
        df['status_cadastro'] = np.where(
            (df['tipo_cliente'] == 'comercio') & (df['cnpj'].isna()), 'PENDENTE', 'OK'
        )

        df.to_csv(caminho_saida, index=False)
        print(f"✅ [TRANSFORM] Dados limpos e prontos na Silver.")

    except Exception as e:
        print(f"❌ [TRANSFORM] Erro: {e}")

if __name__ == "__main__":
    limpar_dados()