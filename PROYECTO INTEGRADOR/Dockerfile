FROM python:3.12-slim 

COPY . /climaApp

WORKDIR /climaApp

RUN pip install -r requirements.txt

CMD [ "python3" ,"main.py" ]
