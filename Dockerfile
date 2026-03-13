# Start with Python 3.11 clean environment
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency files first
# Docker caches this layer → faster rebuilds
COPY pyproject.toml .

# Install uv and dependencies
RUN pip install uv
RUN uv sync

# Copy your actual code
COPY . .

# Expose port 8000
EXPOSE 8000

# Command to run your app
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
