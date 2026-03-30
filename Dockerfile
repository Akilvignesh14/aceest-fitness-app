# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim
RUN apt-get update && apt-get install -y \
    python3-tk \
    libtk8.6 \
    && rm -rf /var/lib/apt/lists/*
# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements file into the container
COPY requirements.txt .

# Step 4: Install dependencies (Flask and Pytest)
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of your application code
COPY . .

# Step 6: Expose port 5000 for the Flask app
EXPOSE 5000

# Step 7: Define the command to run your app
CMD ["python", "app.py"]