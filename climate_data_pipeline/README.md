# Climate Data Pipeline — Weather in Northeast Brazil Capitals (2020–2024)

This project uses **dbt (data build tool)** with **DuckDB** to transform historical weather data obtained from the [Open-Meteo API](https://open-meteo.com/). The dataset contains daily information on maximum and minimum temperatures and precipitation for the **9 capital cities of the Northeast Region of Brazil**, from **2020 to 2024**.

## Objective

To demonstrate, using dbt best practices:

* The ingestion of public data via API (as CSV seed)
* The use of `staging` and `mart` models
* The generation of an annual climate summary per city

---

## Project Flow (Pipeline)

```text
[Open-Meteo API] 
     │
     ▼
[Python Script - fetches and generates CSV in /seeds]
     │
     ▼
[dbt seed]
     │
     ▼
[Model: stg_clima.sql → cleaning and typing]
     │
     ▼
[Model: mart_clima_resumo.sql → aggregations by city and year]
     │
     ▼
[Documentation and tests with schema.yml]
```

---

## Project Structure

```
data_transform/
├── models/
│   ├── staging/
│   │   └── stg_clima.sql           # Cleans and types seed data
│   ├── marts/
│   │   └── core/
│   │       └── mart_clima_resumo.sql  # Aggregations by city and year
│   └── schema.yml                  # Tests and documentation
├── seeds/
│   └── clima_diario_capitais_ne.csv  # Original weather dataset
├── dbt_project.yml
```

---

## Component Explanation

### 1. **Seed**: `clima_diario_capitais_ne.csv`

Contains raw weather data extracted from Open-Meteo. It serves as the starting point of the dbt pipeline. The `seeds/` folder is automatically recognized by dbt.

### 2. **Staging Model**: `stg_clima.sql`

Responsible for:

* Converting data types (e.g., from text to `date`, `float`)
* Normalizing city names (`lower`)
* Structuring the data for later use in marts

### 3. **Mart Model**: `mart_clima_resumo.sql`

Creates an annual summary by capital:

* Average maximum and minimum temperatures
* Total precipitation
* Grouped by `city`, `state`, and `year`

### 4. **Schema.yml**: documentation and tests

Defines:

* The seed source (`source`)
* `not_null` tests for required fields
* Descriptions for models and columns

---

## How to Run

```bash
# 1. Activate environment and install dependencies (with Poetry)
poetry install

# 2. Run dbt commands
poetry run task dbt_seed     # Loads seeds
poetry run task dbt_run      # Executes models
poetry run task dbt_docs     # Generates and serves local documentation
```

> Make sure your `profiles.yml` points to the correct `data_transform.duckdb` file.

---

## Technologies Used

* **dbt-duckdb**: local SQL transformation with lightweight storage
* **Open-Meteo API**: historical weather data via HTTP
* **DuckDB**: columnar analytical database
* **Poetry + Taskipy**: automation and dependency management

---

## Note

This is an educational project designed to demonstrate how to build analytical pipelines using public data and dbt best practices.
