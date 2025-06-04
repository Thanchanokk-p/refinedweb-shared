import duckdb

con = duckdb.connect()
con.execute(r'''
    CREATE OR REPLACE TABLE filtered_primark AS
    SELECT *
    FROM 'parquet_data/*.parquet'
    WHERE
        LOWER(content) LIKE '%primark%' OR
        LOWER(url) LIKE '%primark%' OR
        LOWER(url) LIKE '%primark.com%' OR
        LOWER(url) LIKE '%primark.%'  -- covers localized domains (e.g., .ie, .co.uk)
''')

con.execute(r'''
    COPY filtered_primark TO 'filtered_data/primark.parquet' (FORMAT PARQUET)
''')

print("Filtered + Exported to filtered_data/primark.parquet")