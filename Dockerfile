FROM python:3-alpine3.22
WORKDIR /app
COPY . ${WORKDIR}
RUN pip install -r requirements.txt
USER 65534:65534
CMD /app/label-nodes.py
