FROM python:3

#set env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update
RUN python3 -m pip install requests
RUN mkdir app
ADD q3solution.py /
WORKDIR /app
COPY . /app
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
CMD ["python", "q3solution.py"]

