FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Install necessary packages
RUN apk update && apk add --no-cache \
    openssl \
    && rm -rf /var/cache/apk/*

# Copy server application code
COPY server.py .

# Expose port
EXPOSE 8181

# Set volume
VOLUME ["/serverdata"]

# Start server
CMD ["python", "server.py"]

