FROM continuumio/miniconda3:23.3.1-0

# Set the working directory inside the container
WORKDIR /app

# Copy the environment YAML file to the container
COPY environment.yml .

# Create a Conda environment from the YAML file
RUN conda env create -f environment.yml


# Activate the Conda environment
SHELL ["conda", "run", "-n", "geoenv", "/bin/bash", "-c"]

# Start Jupyter Lab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
