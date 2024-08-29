FROM python:3.7-slim
LABEL maintainer="ibtissam Makdoun <datascienceeveryone772@gmail.com>"
LABEL version="1.0"
LABEL description="This is a Dockerfile for a Python \
            application, it is provided as an example for my course \
            about Docker for Data Science"

# Set the working directory in the container
WORKDIR /data

COPY . /data

RUN pip install numpy pandas scikit-learn juptyer

CMD [ "juptyer", "notebook", "--ip=0.0.0.", "--port=8888", "--no-browser", "--allow-root" ]