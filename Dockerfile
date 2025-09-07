FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# default command overridden by docker-compose
CMD ["flask", "run", "--host=0.0.0.0"]

