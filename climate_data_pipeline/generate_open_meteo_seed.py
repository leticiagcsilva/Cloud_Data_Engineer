import pandas as pd
import requests
from pathlib import Path

capitais_ne = [
    {"cidade": "Aracaju", "uf": "SE", "lat": -10.9472, "lon": -37.0731},
    {"cidade": "Fortaleza", "uf": "CE", "lat": -3.7172, "lon": -38.5433},
    {"cidade": "João Pessoa", "uf": "PB", "lat": -7.1195, "lon": -34.845},
    {"cidade": "Maceió", "uf": "AL", "lat": -9.6658, "lon": -35.735},
    {"cidade": "Natal", "uf": "RN", "lat": -5.7945, "lon": -35.211},
    {"cidade": "Recife", "uf": "PE", "lat": -8.0476, "lon": -34.877},
    {"cidade": "Salvador", "uf": "BA", "lat": -12.9718, "lon": -38.5011},
    {"cidade": "São Luís", "uf": "MA", "lat": -2.5307, "lon": -44.3068},
    {"cidade": "Teresina", "uf": "PI", "lat": -5.0892, "lon": -42.8016},
]

start_date = "2020-01-01"
end_date = "2024-12-31"

Path("seeds").mkdir(exist_ok=True)
dados = []

for cidade in capitais_ne:
    print(f"Baixando dados de {cidade['cidade']} ({cidade['uf']})...")
    url = (
        "https://archive-api.open-meteo.com/v1/archive"
        f"?latitude={cidade['lat']}&longitude={cidade['lon']}"
        f"&start_date={start_date}&end_date={end_date}"
        "&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        "&timezone=America%2FSao_Paulo"
    )

    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        data = r.json()

        df = pd.DataFrame({
            "data": data["daily"]["time"],
            "temp_max": data["daily"]["temperature_2m_max"],
            "temp_min": data["daily"]["temperature_2m_min"],
            "precipitacao": data["daily"]["precipitation_sum"],
        })
        df["cidade"] = cidade["cidade"]
        df["uf"] = cidade["uf"]
        dados.append(df)

    except Exception as e:
        print(f"Erro com {cidade['cidade']}: {e}")

if dados:
    resultado = pd.concat(dados)
    resultado.to_csv("seeds/clima_diario_capitais_ne.csv", index=False)
    print("✅ Arquivo salvo em seeds/clima_diario_capitais_ne.csv")
else:
    print("⚠️ Nenhum dado foi baixado.")
