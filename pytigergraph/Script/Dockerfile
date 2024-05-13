# Use the official Jupyter base image with Python 3
FROM jupyter/base-notebook

# Install pyTigerGraph
RUN pip install pytigergraph

# Expose the port Jupyter Notebook runs on
EXPOSE 8888

# Run Jupyter Notebook
CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
