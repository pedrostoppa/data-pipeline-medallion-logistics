# 📖 Dicionário de Dados - Pipeline de Logística (Medallion)

Este documento detalha a evolução dos dados entre as camadas Bronze, Silver e Gold, descrevendo as transformações e a finalidade de cada coluna.

## 🥉 Camada Bronze (Raw)
*Dados crus extraídos diretamente da fonte (Excel/CSV).*

| Coluna | Descrição | Tipo Original |
| :--- | :--- | :--- |
| **data_venda** | Data da transação | Object |
| **id_venda** | Identificador da venda | Float |
| **tipo_cliente** | B2C (Consumidor) ou B2B (Comércio) | Object |
| **produto** | Nome do item vendido | Object |
| **marca** | Fabricante do produto | Object |
| **quantidade** | Volume de itens vendidos | Float |
| **preco_unitario** | Preço por unidade (com R$) | Object |
| **canal_venda** | Origem do pedido (WhatsApp, Balcão, etc) | Object |
| **forma_pagamento** | Meio de pagamento utilizado | Object |
| **cnpj** | Registro para clientes B2B | Object |

---

## 🥈 Camada Silver (Trusted & Enriched)
*Dados limpos, tipados e com novas colunas de inteligência de negócio.*

| Coluna | Transformação / Regra de Negócio | Tipo Final |
| :--- | :--- | :--- |
| **data_venda** | Conversão para formato temporal padrão | Datetime |
| **id_venda** | Cast para Inteiro (Schema Enforcement) | Integer |
| **quantidade** | Cast para Inteiro | Integer |
| **preco_unitario** | Limpeza de símbolos (R$) e conversão para decimal | Float |
| **valor_total** | **[Nova]** Cálculo: `quantidade * preco_unitario` | Float |
| **status_cadastro** | **[Nova]** REGULAR ou PENDENTE (validação de CNPJ) | String |
| *Outras colunas* | Padronização de texto (Upper case e Strip) | String |

---

## 🥇 Camada Gold (Refined / KPIs)
*Tabela agregada focada em performance de vendas por produto e marca.*

| Coluna | Descrição da Agregação |
| :--- | :--- |
| **produto** | Chave de agrupamento por item |
| **marca** | Chave de agrupamento por fabricante |
| **quantidade** | Soma total do volume vendido (Soma de `quantidade`) |
| **valor_total** | Faturamento bruto acumulado (Soma de `valor_total`) |

---

## 🛠️ Notas de Engenharia
* **Linhagem (Lineage):** A camada Gold remove colunas transacionais (como IDs e formas de pagamento) para otimizar o consumo por ferramentas de BI.
* **Qualidade:** A coluna `status_cadastro` na Silver permite que o time de dados identifique rapidamente falhas na coleta de CNPJ em clientes comerciais.