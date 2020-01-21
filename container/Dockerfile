FROM python:3.7-alpine
MAINTAINER Soichi David Nakahashi <sdn03.tech@gmail.com>

COPY message.py message.py
RUN pip install --upgrade pip && \
    pip install twilio flask gunicorn

EXPOSE 8080
CMD ["gunicorn", "-b", "0.0.0.0:8080", "message:app"]
