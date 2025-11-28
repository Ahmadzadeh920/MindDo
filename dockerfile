FROM python:3.12-slim

WORKDIR /usr/src/core

COPY ./requirements.txt .

RUN pip install -i https://mirror-pypi.runflare.com/simple --no-cache-dir --upgrade -r ./requirements.txt

COPY . .


# Upgrade pip first
RUN pip install --upgrade pip

# Install other dependencies
RUN pip install -r requirements.txt

ENV PYTHONPATH=/usr/src/core
CMD ["uvicorn", "presentation.api.fastapi.main:app", "--host", "0.0.0.0", "--port", "8000"]