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

# optimize image caching
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8082
#CMD [ "waitress-serve", "--port=8082", "app:app"]
CMD ["python3", "remote_exec.py", "8082"]
