# Base image with Java (OpenJDK 17)
FROM openjdk:17

# Install Python 3.12 and pip
RUN apt-get update && apt-get install -y \
    python3.12 python3.12-distutils curl && \
    ln -sf /usr/bin/python3.12 /usr/bin/python && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install --upgrade pip && \
    pip install spacy keybert sentence-transformers

# Download spaCy English model
RUN python -m spacy download en_core_web_sm

# Copy all project files
COPY . .

# Expose port for Jupyter Notebook
EXPOSE 8888

# Launch specific Jupyter Notebook without token
CMD ["jupyter", "notebook", "notebooks/1_refinedweb-analysis-1.ipynb", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''"]
