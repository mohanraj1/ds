FROM python:3.5
# Install flask and redis
RUN pip install Flask==0.11.1 redis==2.10.5
RUN useradd -ms /bin/bash mohand
USER mohand
WORKDIR /app
# Commenting because we have defined volumne in the docker-compose yml
# COPY app /app
CMD ["python", "app.py"] 
