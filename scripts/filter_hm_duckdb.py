import duckdb

con = duckdb.connect()
con.execute(r"""
    CREATE OR REPLACE TABLE filtered_hm AS
    SELECT *
    FROM 'parquet_data/*.parquet'
    WHERE
        (
            LOWER(content) LIKE '%h&m%' OR
            LOWER(url) LIKE '%h&m%' OR
            LOWER(url) LIKE '%hm.com%' OR
            LOWER(url) LIKE '%hm%' OR
            LOWER(url) LIKE '%hm.%'  -- keep as fallback
        )
        AND (
            LOWER(content) LIKE '%clothing%' OR
            LOWER(content) LIKE '%fashion%' OR
            LOWER(content) LIKE '%shop%' OR
            LOWER(url) LIKE '%hm.com%'
        )
""")

con.execute(r"""
    COPY filtered_hm TO 'filtered_data/hm.parquet' (FORMAT PARQUET)
""")

print("Filtered + Exported to filtered_data/hm.parquet")
