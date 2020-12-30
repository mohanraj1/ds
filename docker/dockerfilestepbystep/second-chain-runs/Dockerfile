# Base image
FROM debian:jessie

# Command to execute in linux terminal; y because we can't answer the prompt
# Best Pratice
#   Chain Runs to reduce image layers
#   Order install packages in alphabetical order
RUN apt-get update && apt-get install -y \
    git \    
    vim

CMD ["echo", "hello world"]