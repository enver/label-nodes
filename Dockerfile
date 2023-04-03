FROM python:alpine3.17
WORKDIR /app
COPY . ${WORKDIR}
RUN pip install -r requirements.txt
USER 65534:65534
CMD /app/label-node.py
