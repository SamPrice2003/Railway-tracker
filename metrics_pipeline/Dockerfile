FROM public.ecr.aws/lambda/python:3.12

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY extract.py .

COPY transform.py .

COPY load.py .

COPY pipeline.py .

CMD ["pipeline.handler"]
