FROM python:3

RUN apt-get update
RUN pip3 install requests
RUN mkdir app
WORKDIR "/app"
COPY q3solution.py app/q3solution.py
CMD [ "q3solution.py" ]
ENTRYPOINT ["python3"]
