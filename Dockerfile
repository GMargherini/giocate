FROM python:3.14-rc-alpine3.21
WORKDIR /app

RUN pip install nicegui
RUN pip install numpy
RUN pip install matplotlib

COPY src ./app/src
EXPOSE 8080

CMD ["python", "/app/src/main.py"]
