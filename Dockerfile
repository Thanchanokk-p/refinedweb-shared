# Use base image with Java (for PySpark)
FROM openjdk:11

# Install Python 3.12 and pip
RUN apt-get update && apt-get install -y \
    python3.12 python3.12-distutils curl && \
    ln -s /usr/bin/python3.12 /usr/bin/python && \
    curl -sS https://bootstrap.pypa.io/get-pip.py | python

# Set working directory
WORKDIR /app

# Copy requirements file and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose port for Jupyter Notebook
EXPOSE 8888

# Default command: run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--no-browser"]
