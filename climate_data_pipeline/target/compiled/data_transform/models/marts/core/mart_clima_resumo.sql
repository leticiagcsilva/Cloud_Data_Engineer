with base as (
    select
        cidade,
        uf,
        extract(year from data) as ano,
        avg(temp_max) as media_temp_max,
        avg(temp_min) as media_temp_min,
        sum(precipitacao) as total_precipitacao
    from "data_transform"."main"."stg_clima"
    group by cidade, uf, ano
)
select * from base
order by cidade, ano