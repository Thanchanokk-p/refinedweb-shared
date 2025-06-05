#  Use jupyter/pyspark-notebook image (from Jupyter Docker Stacks)
FROM jupyter/pyspark-notebook:latest

# Switch to root user to install Python
USER root

# Set working directory inside container - define own WORKDIR as /app 
# Everything inside container will operate in /app
WORKDIR /app

# Copy all project files (includes data/, scripts/, notebooks/, etc.)
COPY . .

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt
    

# Download spaCy English model (optional: keep if used in notebook)
RUN python3 -m spacy download en_core_web_sm

# Expose port for Jupyter Notebook
EXPOSE 8888

# Start the notebook when the container runs - open 1st notebook 
CMD ["jupyter", "notebook", "notebooks/1_refinedweb-analysis-1.ipynb", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''"]