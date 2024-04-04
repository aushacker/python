FROM registry.access.redhat.com/ubi9/python-311

ADD app-src .
RUN chown -R 1001:0 ./
USER 1001

RUN python3 -m pip install --upgrade pip && \
    pip install kubernetes

# Run the application
#ENTRYPOINT ["uvicorn"]
#CMD ["main:app", "--host", "0.0.0.0", "--reload"]
