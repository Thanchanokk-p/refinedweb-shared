# Base image with Java (OpenJDK 17)
FROM openjdk:17

# Install Python 3.12 and pip
RUN apt-get update && apt-get install -y \
    python3.12 python3.12-distutils curl wget && \
    ln -sf /usr/bin/python3.12 /usr/bin/python && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Download spaCy model
RUN python -m spacy download en_core_web_sm

# Copy all project files
COPY . .

# Copy and set permissions for shell script
COPY download_parquet.sh /app/download_parquet.sh
RUN chmod +x /app/download_parquet.sh

# Step 1: Download data via shell script
RUN /app/download_parquet.sh

# Step 2: Run all filtering scripts (DuckDB-based)
RUN python /app/scripts/filter_hm_duckdb.py && \
    python /app/scripts/filter_primark_duckdb.py && \
    python /app/scripts/filter_zara_duckdb.py

# Expose port for Jupyter Notebook
EXPOSE 8888

# Launch notebook
CMD ["jupyter", "notebook", "notebooks/1_refinedweb-analysis-1.ipynb", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''"]
