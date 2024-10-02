FROM python:3.10.12
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY . /app
RUN python3 -m venv /opt/.venv
RUN /opt/.venv/bin/pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["/app/entrypoint.sh"]
#CMD ["/app/.venv/bin/python", "app.py"]