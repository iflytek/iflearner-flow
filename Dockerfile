FROM python:3.9

COPY . /iflearner-flow

RUN pip install -r /iflearner-flow/requirements.txt -i https://pypi.douban.com/simple
