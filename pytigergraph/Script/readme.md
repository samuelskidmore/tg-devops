README.md
markdown
Copy code
# Jupyter Notebook with pyTigerGraph

This project provides a Docker setup for running a Jupyter Notebook server that includes the `pyTigerGraph` library for interacting with TigerGraph databases.

## Prerequisites

- Docker installed on your machine. Visit [Docker's official site](https://www.docker.com/products/docker-desktop) for installation instructions.

## Getting Started

### Pulling the Base Image

Before building your Docker image, you need to pull the base image from Docker Hub:

```bash
docker pull jupyter/base-notebook
Building the Docker Image
To build the Docker image, navigate to the directory containing your Dockerfile and run the following command:

bash
Copy code
docker build -t jupyter-pytigergraph .
Running the Docker Container
After the image has been built, you can start a container using:

bash
Copy code
docker run -p 8888:8888 jupyter-pytigergraph
This command maps port 8888 of the container to port 8888 on your host. You can access the Jupyter Notebook by visiting http://localhost:8888 in your web browser.

Usage
Once your Jupyter Notebook server is running, you can use it to develop and run Python code that interacts with TigerGraph databases using the pyTigerGraph library.

Security
For production environments, it's recommended to secure your Jupyter Notebook server. You can set up a password or token by modifying the CMD line in the Dockerfile or configuring Jupyter Notebook settings directly.

Support
For issues related to Docker setup or usage, refer to Docker documentation. For issues specific to pyTigerGraph, consult the pyTigerGraph GitHub repository.