FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy only requirements first (use Docker layer caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy app code and model files
COPY api/ api/
COPY model/ model/

# Expose the port FastAPI will run on
EXPOSE 8000

# Run FastAPI app (main.py inside api/)
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
