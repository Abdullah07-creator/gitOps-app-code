# Step 1: Use a lightweight official Python base image
FROM python:3.10-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy dependency requirements first to leverage Docker layer caching
COPY requirements.txt .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the application code into the container
COPY app.py .

# Step 6: Expose port 5000 so Docker documents which port the app listens on
EXPOSE 5000

# Step 7: Specify default command to run the Python application
CMD ["python", "app.py"]
