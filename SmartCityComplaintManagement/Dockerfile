# Use a slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Set environment variables (if needed)
ENV PYTHONUNBUFFERED=1

# Default command
CMD ["sh", "run_etl.sh"]
