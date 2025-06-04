# RefinedWeb Analysis

This project explores the potential of enhancing LLM (Large Language Model) performance on **RefinedWeb** — a brand-specific, curated web dataset tailored for retail and enterprise-focused use cases.

### What is RefinedWeb?
RefinedWeb is a cleaned, filtered, and deduplicated web crawl dataset, optimized for training and evaluating large-scale language models. It includes high-quality, domain-specific text content suitable for commercial applications such as brand intelligence, product sentiment analysis, and customer service automation.

---

## Project Objectives

The goal of this project is to improve the visibility and relevance of AI-powered search and insights tools by training models on focused web content. Specifically, the analysis helps:

- Improve brand visibility 
- Support internal tools like search assistants and chatbots
- Provide actionable insights in areas such as:
  - Brand perception
  - Competitive intelligence
  - SEO performance
  - Campaign strategy optimization

---

##  Technical Notes

- The project currently runs with limited memory and compute resources. For this reason, initial development is done a small scale.
- **Apache Spark (PySpark)** is required to enable distributed data processing.
- The server environment has been upgraded with AI8 server to support larger-scale operations.
- Future iterations may incorporate cloud-based or cluster-backed execution for larger models and datasets.

---

## 📁 Project Structure

```text
refinedweb-shared/
├── notebooks/             # Jupyter Notebooks for data exploration and analysis
├── scripts/               # Python scripts (e.g., DuckDB filters)
├── data/
│   ├── parquet_data/      # Raw downloaded data
│   └── filtered_data/     # Cleaned and filtered output
├── download_parquet.sh    # Script to pull data from HuggingFace
├── paths.txt              # List of data paths
├── requirements.txt       # Python dependencies
├── Dockerfile             # Docker image setup
├── .gitignore
└── README.md           
