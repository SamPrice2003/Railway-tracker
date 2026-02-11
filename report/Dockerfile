FROM public.ecr.aws/lambda/python:3.12

RUN dnf install -y gcc

RUN dnf install -y cairo-devel pkg-config python3-devel

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY upload_to_s3.py .

COPY report_html.py .

COPY metrics.py .

COPY report.py .

CMD ["report.handler"]