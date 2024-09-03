FROM python:3

LABEL maintainer="Ibtissam Makdoun <datascienceeveryone@gmail.com>"
LABEL version="0.1"
LABEL description="Notebook and data (.csv file) to provide a summary \
                  of the total medals won by participating countries \
                  in the 2008 Summer Olympics."

WORKDIR /data


# Copy all files from the current directory to /data in the container
COPY . /data

# Install the required Python packages
RUN pip install pandas numpy matplotlib seaborn jupyter

# Expose port 8888 for Jupyter Notebook
EXPOSE 8888

# Command to run Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
