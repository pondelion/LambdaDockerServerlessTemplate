FROM public.ecr.aws/lambda/python:3.8

RUN yum install -y git
RUN python -m pip install --upgrade pip
COPY ./handler.py .
COPY ./handler2.py .
COPY ./requirements.txt .
RUN pip install -r requirements.txt
CMD ["handler.handler"]
