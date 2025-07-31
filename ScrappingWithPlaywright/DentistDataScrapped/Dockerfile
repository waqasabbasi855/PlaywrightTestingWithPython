# Use an official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies for Playwright and Xvfb
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    ca-certificates \
    curl \
    xvfb \
    libnss3 \
    libatk-bridge2.0-0 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    libgtk-3-0 \
    libasound2 \
    fonts-liberation \
    libappindicator3-1 \
    xauth \
    && rm -rf /var/lib/apt/lists/*

# Install Playwright
RUN pip install --upgrade pip && pip install playwright python-dotenv
RUN playwright install --with-deps

# Set working directory
WORKDIR /app

# Copy your code
COPY . .

# Create output directory
RUN mkdir -p /app/output

# Set command to run script with Xvfb
CMD ["xvfb-run", "-a", "python", "main.py"]
