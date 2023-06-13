FROM python:3.9-alpine

# Create app directory
WORKDIR /app

# Install app dependencies
COPY requirements.txt ./

RUN apk update \
    && apk add --no-cache --virtual .build-deps ca-certificates make gcc g++ cyrus-sasl-dev

#RUN apt-get install libsasl2-dev
RUN pip install -r requirements.txt

# Bundle app source
COPY . .

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]