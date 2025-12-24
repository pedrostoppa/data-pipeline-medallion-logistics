# Importando as funções dos seus scripts que estão dentro da pasta 'etl'
from etl.extract import gerar_massa_mensal
from etl.transform import limpar_dados
from etl.aggregate import criar_kpis

def executar_sistema_completo():
    print("\n" + "="*40)
    print("🚀 INICIANDO PIPELINE: DEPÓSITO DE ÁGUA E GÁS")
    print("="*40 + "\n")
    
    # PASSO 1: EXTRAÇÃO
    # Gera 20.000 linhas com colunas: id_venda, marca, cnpj, etc.
    gerar_massa_mensal(mes=1, ano=2024)
    
    # PASSO 2: TRANSFORMAÇÃO
    # Limpa os R$, converte datas e aplica regras de negócio (status do CNPJ)
    limpar_dados()
    
    # PASSO 3: AGREGAÇÃO (Camada Gold)
    # Cria os resumos prontos para o Power BI (Faturamento por Marca/Produto)
    criar_kpis()
    
    print("\n" + "="*40)
    print("✨ SUCESSO! O ciclo Medalhão foi concluído.")
    print("📊 Os dados já estão na pasta 'gold' para o Power BI.")
    print("="*40)

if __name__ == "__main__":
    executar_sistema_completo()