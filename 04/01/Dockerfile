FROM continuumio/miniconda3

LABEL maintainer="Ibtissam Makdoun <datascienceeveryone772@gmail.com>"
LABEL description="Dev environment for machine learning and data science team \
                  with access to shared data in network drive."

WORKDIR /data

RUN conda create -n myenv python=3.7.3 -y && \
      conda install -n myenv jupyter pandas==0.24.2 seaborn==0.9.0 -y && \
      conda clean -y --all
                  
# Activate the environment
ENV PATH /opt/conda/envs/myenv/bin:$PATH
                  
EXPOSE 8888
                  
VOLUME /data
                  
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]