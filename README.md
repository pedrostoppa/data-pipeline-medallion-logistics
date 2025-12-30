# 📊 Data Pipeline — Distribuidora de Água e Gás (ETL Profissional)

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Library-Pandas-150458.svg)](https://pandas.pydata.org/)
[![Architecture](https://img.shields.io/badge/Architecture-Medallion-gold.svg)](#-arquitetura-do-projeto)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/seu-usuario/)

Projeto completo de **ETL (Extract, Transform, Load)** simulando o contexto real de uma distribuidora de água e gás. Desenvolvido para consolidar conceitos de Engenharia de Dados, o pipeline processa dados brutos, aplica regras de negócio e gera bases analíticas prontas para consumo.



---

## 🎯 Objetivo do Projeto
- **Simular um cenário real de negócio** (B2C e B2B).
- **Aplicar boas práticas de ETL** com Python e Pandas.
- **Gerar camadas de dados organizadas** (Bronze, Silver e Gold) seguindo a Arquitetura Medalhão.
- **Servir como projeto âncora de portfólio** para demonstração de competências técnicas.

---

## 🏗️ Arquitetura e Governança
O projeto foi desenhado sob os princípios de **consistência e idempotência**. A cada execução do `main.py`, os dados são reprocessados, garantindo que a versão mais recente dos indicadores esteja disponível sem duplicidade.

### As Camadas:
* **🥉 Bronze (Raw):** Dados brutos conforme extraídos da fonte.
* **🥈 Silver (Trusted):** Dados limpos, tipados e padronizados.
* **🥇 Gold (Refined):** Dados agregados em KPIs prontos para Dashboards.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.12+**
- **Pandas & NumPy:** Processamento e lógica condicional.
- **Git / GitHub:** Versionamento.
- **Modularização:** Scripts separados por responsabilidade (Extração, Transformação e Agregação).

---

## 🗂️ Estrutura do Projeto

```text
├── data/
│   ├── bronze/    # Input original (20k registros)
│   ├── silver/    # Dados Trusted (Limpos e Padronizados)
│   └── gold/      # Dados Refined (KPIs de Negócio)
├── docs/          # Dicionário de Dados e Regras de Negócio
├── etl/
│   ├── extract.py    # Gerador/Extrator de massa de dados
│   ├── transform.py  # Limpeza e Schema Enforcement
│   └── aggregate.py  # Criação de KPIs analíticos
├── main.py        # Orquestrador do Pipeline
└── requirements.txt
```
---

## 🛡️ Qualidade e Governança (Data Quality)
Para garantir a confiabilidade do output final, o pipeline implementa:

- **Schema Enforcement:** Validação de tipos de colunas críticas (ID, Preço, Data) antes da carga.

- **Data Sanitization:** Remoção de caracteres especiais (R$, vírgulas) e padronização de strings.

- **Tratamento de Exceções:** Logs informativos que permitem rastrear falhas em cada etapa.

---

## 📈 Principais KPIs Gerados
1. **Faturamento por Produto/Marca:** Identificação dos itens mais rentáveis (Curva ABC).

2. **Performance de Canais:** Análise de vendas (WhatsApp, Balcão, Telefone).

3. **Validação B2B:** Identificação de pendências cadastrais (CNPJ ausente).

---

## ▶️ Como Executar o Projeto
**1. Clone o repositório:**

```text
git clone https://github.com/pedrostoppa/data-pipeline-medallion-logistics.git
```

**2. Instale as dependências:**

```text
pip install -r requirements.txt
```

**3. Execute o orquestrador:**
```text
python main.py
```
---
## 🚀 Roadmap (Próximos Passos)
- [ ] Integração com banco de dados SQL (PostgreSQL).

- [ ] Criação de dashboards dinâmicos no Power BI.

- [ ] Orquestração do pipeline com Apache Airflow.
---
## 👤 Autor
**Pedro Stoppa** - Engenheiro de Dados | Python & Business Intelligence

[![Linkedin](https://img.shields.io/badge/Linkedin-blue.svg)](https://www.linkedin.com/in/pedro-stoppa/)
[![Email](https://img.shields.io/badge/Email-red.svg)](pedrostoppa.dev@gmail.com)
[![WhatsApp](https://img.shields.io/badge/Whatsapp-gred.svg)](https://wa.me/558694818921)