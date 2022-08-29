FROM python:3.9

RUN mkdir -p /data/iflearner_flow/python/
COPY iflearner_flow_federate /data/iflearner_flow/python/iflearner_flow_federate
COPY iflearner_job /data/iflearner_flow/python/iflearner_job
ENV PYTHONPATH=/data/iflearner_flow/python:${PYTHONPATH}
WORKDIR /data/iflearner_flow/python/iflearner_flow_federate
RUN pip3 install -r ../iflearner_job/requirements.txt -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple && \
pip3 install -r requirements.txt -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com/simple
EXPOSE 1236
CMD ["python3" ,"app.py"]