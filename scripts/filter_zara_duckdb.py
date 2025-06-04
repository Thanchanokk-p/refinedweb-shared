import duckdb

con = duckdb.connect()
con.execute(r"""
    CREATE OR REPLACE TABLE filtered_zara AS
    SELECT *
    FROM 'parquet_data/*.parquet'
    WHERE
        (
            LOWER(content) LIKE '%zara%' OR
            LOWER(url) LIKE '%zara%' OR
            LOWER(url) LIKE '%zara.com%' OR
            LOWER(url) LIKE '%zara.%'  -- covers localized domains (e.g., .ie, .co.uk)
        )
        AND (
            LOWER(content) LIKE '%clothing%' OR
            LOWER(content) LIKE '%fashion%' OR
            LOWER(content) LIKE '%shop%' OR
            LOWER(url) LIKE '%zara%'
        )
""")

con.execute(r"""
    COPY filtered_zara TO 'filtered_data/zara.parquet' (FORMAT PARQUET)
""")

print("Filtered + Exported to filtered_data/zara.parquet")
