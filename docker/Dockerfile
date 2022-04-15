####
# Build the image with:
# docker build -f docker/Dockerfile -t python/python-deploy .
#
# Then run the container using:
#
# docker run -i --rm -p 8081:8081 python/python-deploy
####
FROM python

WORKDIR /projects

RUN python3 -m venv venv
RUN . venv/bin/activate

RUN cd ../../../
COPY requirements.txt /tmp/build/inputs/requirements.txt

# optimize image caching
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8081
CMD [ "waitress-serve", "--port=8081", "app:app"]

