# Projeto: data\_transform — Clima nas Capitais do Nordeste (2020–2024)

Este projeto utiliza **dbt (data build tool)** com **DuckDB** para transformar dados climáticos históricos obtidos via [Open-Meteo API](https://open-meteo.com/). O dataset contém informações diárias de temperatura máxima, mínima e precipitação para as **9 capitais da Região Nordeste do Brasil**, entre **2020 e 2024**.

## Objetivo

Demonstrar, por meio de boas práticas com dbt:

* A ingestão de dados públicos via API (como seed CSV)
* O uso de modelos `staging` e `mart`
* A geração de um resumo climático anual por cidade

---

## Fluxo do Projeto (Pipeline)

```text
[Open-Meteo API] 
     │
     ▼
[Script Python - coleta e gera CSV em /seeds]
     │
     ▼
[dbt seed]
     │
     ▼
[Modelo: stg_clima.sql → limpeza e tipagem]
     │
     ▼
[Modelo: mart_clima_resumo.sql → agregações por cidade e ano]
     │
     ▼
[Documentação e testes com schema.yml]
```

---

## Estrutura do Projeto

```
data_transform/
├── models/
│   ├── staging/
│   │   └── stg_clima.sql           # Limpeza e tipagem dos dados do seed
│   ├── marts/
│   │   └── core/
│   │       └── mart_clima_resumo.sql  # Agregações por cidade e ano
│   └── schema.yml                  # Testes e documentação
├── seeds/
│   └── clima_diario_capitais_ne.csv  # Dataset climático original
├── dbt_project.yml
```

---

## Explicação dos Componentes

### 1. **Seed**: `clima_diario_capitais_ne.csv`

Contém os dados brutos extraídos da Open-Meteo. Serve como ponto de partida do pipeline dbt. A pasta `seeds/` é automaticamente reconhecida pelo dbt.

### 2. **Modelo Staging**: `stg_clima.sql`

Responsável por:

* Converter tipos (de texto para `date`, `float`)
* Normalizar nomes de cidade (`lower`)
* Padronizar a estrutura para uso posterior em marts

### 3. **Modelo Mart**: `mart_clima_resumo.sql`

Cria um resumo anual por capital:

* Média de temperaturas máximas e mínimas
* Soma da precipitação
* Agrupado por `cidade`, `uf` e `ano`

### 4. **Schema.yml**: documentação e testes

Define:

* A origem do seed (`source`)
* Testes de `not_null` para campos obrigatórios
* Descrições dos modelos e colunas

---

## Como Executar

```bash
# 1. Ativar ambiente e instalar dependências (com Poetry)
poetry install

# 2. Rodar os comandos dbt
poetry run task dbt_seed     # Carrega os seeds
poetry run task dbt_run      # Executa os modelos
poetry run task dbt_docs     # Gera e serve a documentação local
```

> Certifique-se de que o seu `profiles.yml` aponta para o arquivo `data_transform.duckdb` corretamente.

---

## Tecnologias Usadas

* **dbt-duckdb**: transformação SQL local com armazenamento leve
* **Open-Meteo API**: dados climáticos históricos via HTTP
* **DuckDB**: banco local analítico em formato colunar
* **Poetry + Taskipy**: automação e gerenciamento de dependências

---

## Nota

Desenvolvido por Letícia Gomes C. S.

Este projeto é educacional e visa demonstrar o uso de pipelines analíticos com dados públicos e boas práticas com dbt.
