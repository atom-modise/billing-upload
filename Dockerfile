FROM python:3.10.11-alpine

# set working dir
WORKDIR /billing

# set root dir to path
# ENV PATH="/billing/:$PATH"

# copy dependencies and install them
COPY ./requirements.txt /billing/requirements.txt

RUN pip install -r requirements.txt


# copy project files
COPY ./ /billing

# switch to non-root user
RUN adduser -D atom && chown -R atom /billing
USER atom

# expose port
EXPOSE 8000

ENV PATH=$PATH:/usr/local/bin

CMD ["uvicorn", "main:app", "--bind=0.0.0.0:8000", "--log-level=info"]