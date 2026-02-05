# Use the official Microsoft Playwright image with Python
FROM mcr.microsoft.com/playwright/python:v1.40.0-jammy

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure Playwright browsers are installed
RUN playwright install chromium

# Copy the entire project structure
COPY . .

# Set the PYTHONPATH so the 'src' folder is recognized
ENV PYTHONPATH="/app"

# Command to run tests (API key must be passed at runtime)
CMD ["pytest", "-s", "tests/test_dynamic_ui.py"]