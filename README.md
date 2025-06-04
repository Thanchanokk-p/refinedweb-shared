# 🔍 RefinedWeb Analysis

This project explores the potential of enhancing LLM (Large Language Model) performance on **RefinedWeb** — a brand-specific, curated web dataset tailored for retail and enterprise-focused use cases.

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

## ⚙️ Technical Notes

- The current setup uses limited compute resources; development runs at small scale.
- **Apache Spark (PySpark)** is used in early-stage processing for scalability and parallelism.
- AI8 servers are available for future scale-up or distributed execution.
- Cloud-native extensions may be added in the future for large model training.

---

## 📁 Project Structure

```text
refinedweb-shared/
├── notebooks/                    
│   ├── 1_refinedweb-analysis.ipynb         # Spark-based data download + preprocessing
│   └── 2_refinedweb-analysis_nlp.ipynb     # NLP modeling without Spark
├── scripts/                     # Python/DuckDB scripts for filtering
├── data/
│   ├── parquet_data/            # Raw downloaded data
│   └── filtered_data/           # Cleaned output
├── download_parquet.sh          # Script to pull data from HuggingFace
├── paths.txt                    # List of HuggingFace dataset URLs
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker setup
└── README.md                    # Project overview
