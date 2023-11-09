FROM registry.access.redhat.com/ubi9/python-311

USER 0
RUN dnf upgrade -y && \
    dnf clean all

ADD app-src .
RUN chown -R 1001:0 ./
USER 1001

RUN pip install -U "pip>=23.3" && \
    pip install -r requirements.txt

# Run the application
ENTRYPOINT ["uvicorn"]
CMD ["main:app", "--host", "0.0.0.0", "--reload"]
