FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./logging.yml /code/logging.yml

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["uvicorn", "src.main.application:core_module", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]