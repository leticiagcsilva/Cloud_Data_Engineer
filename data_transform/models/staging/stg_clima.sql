with raw as (
    select
        cast(data as date) as data,
        lower(cidade) as cidade,
        uf,
        cast(temp_max as float) as temp_max,
        cast(temp_min as float) as temp_min,
        cast(precipitacao as float) as precipitacao
    from {{ source('clima', 'clima_diario_capitais_ne') }}
)
select * from raw
