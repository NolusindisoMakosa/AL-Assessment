FROM python:3

#set eb
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV URL 'url'

RUN apt-get update
RUN pip3 install requests
RUN mkdir app
ADD q3solution.py /
WORKDIR "/app"
COPY q3solution.py app/q3solution.py
ENV / q3solution.py
CMD [ "/q3solution.py" ]
ENTRYPOINT ["python3"]

