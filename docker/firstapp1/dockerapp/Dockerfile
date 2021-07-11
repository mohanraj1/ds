# Base image
FROM python:3.5
# Install Flask
RUN pip install Flask==0.11.1
# Add a new user admin. 
# ms option creates default home directory for admin 
# We are setting default shell to bash
RUN useradd -ms /bin/bash admin
# running app server under admin. 
# always run non-prvileged user to run the app server in the container.
# otherwise it runs as a root within the container. 
# uuid is same for container and root
USER admin
# Working directory for copy and cmd
WORKDIR /app
# Copy app dir to container
COPY app /app
# Use the relative directory to reference app.py
CMD ["python", "app.py"] 
