# 🔍 RefinedWeb Analysis

This project explores the potential of enhancing LLM (Large Language Model) performance using **RefinedWeb** — a brand-specific, curated web dataset tailored for retail and enterprise-focused use cases.

---

## 📚 What is RefinedWeb?

RefinedWeb is a cleaned, filtered, and deduplicated web crawl dataset optimized for training and evaluating large-scale language models. It includes high-quality, domain-specific text content suitable for commercial applications such as:

- Brand intelligence  
- Product sentiment analysis  
- Customer service automation  

---

## 🎯 Project Objectives

The main objective is to boost visibility and relevance for AI-powered search and insight tools by fine-tuning models on focused web content. This supports:

- Improved brand visibility  
- Enhanced internal tools (e.g., search assistants, chatbots)  
- Actionable business insights in:
  - Brand perception  
  - Competitive intelligence  
  - SEO performance  
  - Campaign strategy optimization  

---

## ⚙️ Environment Versions

This project was tested using the following versions:

```python
Python: 3.12.8 [conda-forge, GCC 13.3.0]  
NumPy: 1.26.4  
Pandas: 2.2.3  
PySpark: 4.0.0
```
Ensure your local or cloud environment matches or is compatible with these versions to avoid compatibility issues, especially with PySpark.

## 🗂️ Project Structure
```bash
refinedweb-shared/
├── data/
│   ├── csv_data/          # Intermediate processed CSVs
│   ├── filtered_data/     # Cleaned data after brand filtering
│   ├── parquet_data/      # Raw files from HuggingFace
│   └── paths.txt          # List of remote .parquet file URLs
│
├── notebooks/
│   ├── 1_refinedweb-analysis.ipynb       # Spark-based EDA and filtering
│   └── 2_refinedweb_analysis_nlp.ipynb   # BERT modeling and text analytics
│
├── scripts/
│   ├── filter_hm_duckdb.py
│   ├── filter_primark_duckdb.py
│   ├── filter_zara_duckdb.py
│   └── sparkcc.py                        # Spark job for processing
│
├── Dockerfile
├── get-docker.sh
├── download_parquet.sh
├── requirements.txt
├── docker-compose.yml
└── README.md


---

## 📊 Data Loading Notes

There are two main ways to load data:

- You can **skip process 2 (Loading the Data)** and start directly from **3. Data Exploration**, using the pre-downloaded files and filters.
- Alternatively, to replicate the full pipeline:
  1. Use `download_parquet.sh` to download data from the URLs listed in `data/paths.txt`.
  2. Use DuckDB or PySpark to query and filter the data (brand-specific scripts are in the `scripts/` folder).

### Filter modules provided:

- `filter_hm_duckdb.py`  
- `filter_primark_duckdb.py`  
- `filter_zara_duckdb.py`  

These scripts help manage memory and temporary files more efficiently during preprocessing.

---

### 🗃️ Data Folders

These directories are part of the project structure, but their contents (e.g., `.csv`, `.parquet`) are excluded from version control via `.gitignore`. You will find `.gitkeep` files to preserve their presence in the repository:
```bash
data/
├── csv_data/ # Stores intermediate CSVs
├── filtered_data/ # Output from Spark/DuckDB filtering
├── parquet_data/ # Raw files downloaded from HuggingFace
```

Make sure your preprocessing or download scripts populate these folders as needed.

---

## 🚀 Getting Started

### 🛠️ Install Dependencies

```bash
pip install -r requirements.txt
```
Or inside a Jupyter Notebook:
```bash
!pip install -r ../requirements.txt
```


🐳 Run via Docker
```bash
# Build the Docker image
docker build -t refinedweb-env .

# Run the container and expose Jupyter
docker run -it -p 8888:8888 refinedweb-env
```

Navigate to http://localhost:8888 to open the notebook interface.

## Run the container and expose Jupyter on port 8888
docker run -it -p 8888:8888 refinedweb-env

Once running, open your browser and go to:  
[http://localhost:8888](http://localhost:8888)

You should see the Jupyter Notebook interface. The first notebook to open is:
notebooks/1_refinedweb-analysis.ipynb


