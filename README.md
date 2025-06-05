# 🔍 RefinedWeb Analysis

This project explores the potential of enhancing LLM (Large Language Model) performance on **RefinedWeb** — a brand-specific, curated web dataset tailored for retail and enterprise-focused use cases.
There are multiple notebooks follow ตามเลขของ notebook, the project separategin notebook to handle xxxx and separate as each tasks
---

## 📚 What is RefinedWeb?

RefinedWeb is a cleaned, filtered, and deduplicated web crawl dataset, optimized for training and evaluating large-scale language models. It includes high-quality, domain-specific text content suitable for commercial applications such as:

- Brand intelligence
- Product sentiment analysis
- Customer service automation

---

## 🎯 Project Objectives

The goal of this project is to improve the visibility and relevance of AI-powered search and insight tools by training models on focused web content. Specifically, this helps:

- Improve brand visibility
- Support internal tools like search assistants and chatbots
- Provide actionable insights in:
  - Brand perception
  - Competitive intelligence
  - SEO performance
  - Campaign strategy optimization

---
```
## 🗂️ Project Structure
refinedweb-shared/
├── data/ # Input/output data folders (excluded from Git)
│ ├── csv_data/ # Stores intermediate CSVs (e.g., transformed features)
│ ├── filtered_data/ # Cleaned output after filtering or deduplication
│ └── parquet_data/ # Raw downloaded files from HuggingFace (referenced in paths.txt)
│ └── paths.txt # List of remote .parquet file URLs
│
├── notebooks/ # Jupyter Notebooks for preprocessing and modeling
│
├── scripts/ # Python scripts for filtering, Spark/duckdb logic
│ ├── filter_*.py # Brand-specific filter scripts
│ └── sparkcc.py # Spark job for counting or transforming content
│
├── Dockerfile # Docker setup for reproducible environment
├── get-docker.sh # Helper script to install Docker (optional)
├── download_parquet.sh # Shell script to download parquet files listed in paths.txt
├── requirements.txt # Python dependencies
└── README.md # Project documentation and instructions
```
---

## ⚙️ Technical Notes

- Development currently runs on limited compute resources for prototyping.
- **Apache Spark (PySpark)** is used for scalable preprocessing of large datasets.
- AI8 servers are supported for scaled or distributed computation.
- Cloud-native components and large-model training extensions may be added later.
- A **Dockerfile** is provided for reproducible environments.
- An optional `get-docker.sh` script is available for installing Docker on compatible systems.

---

## 🚀 Getting Started

### 📦 Run via Docker 

If Docker is already installed:

```bash
# Build the Docker image
docker build -t refinedweb-env .

# Run the container and expose Jupyter on port 8888
docker run -it -p 8888:8888 refinedweb-env

Once running, open your browser and go to:  
[http://localhost:8888](http://localhost:8888)

You should see the Jupyter Notebook interface. The first notebook to open is:
notebooks/1_refinedweb-analysis.ipynb


 You can edit the `CMD` in the `Dockerfile` if you want to launch a different notebook by default.

---

### 🗃️ Data Folders

These directories are part of the project structure, but their contents (e.g., `.csv`, `.parquet`) are excluded from version control via `.gitignore`. You will find `.gitkeep` files to preserve their presence in the repository:

data/
├── csv_data/ # Stores intermediate CSVs
├── filtered_data/ # Output from Spark/DuckDB filtering
├── parquet_data/ # Raw files downloaded from HuggingFace


Make sure your preprocessing or download scripts populate these folders as needed.

---

### ⚙️ Optional: Setup Docker

If Docker is not installed yet, you may use the helper script:

```bash
bash get-docker.sh

