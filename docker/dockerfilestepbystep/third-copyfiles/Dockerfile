# Base image
FROM debian:jessie

# Command to execute in linux terminal; y because we can't answer the prompt
# Best Pratice
#   Chain Runs to reduce image layers
#   Order install packages in alphabetical order
RUN apt-get update && apt-get install -y \
    git \    
    vim

# Copy the file from the build context to src folder in the container
COPY abc.txt /src/abc.txt