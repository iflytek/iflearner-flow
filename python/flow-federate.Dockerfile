FROM python:3.9

COPY iflearner_flow_federate /data/iflearner-flow/python/iflearner_flow_federate
COPY iflearner_job /data/iflearner-flow/python/iflearner_job

RUN python3 -m pip install --upgrade pip && pip install -Ur /data/iflearner-flow/python/iflearner_job/requirements.txt --index-url http://pypi.douban.com/simple --trusted-host pypi.douban.com \
&& pip install -Ur /data/iflearner-flow/python/iflearner_flow_federate/requirements.txt --index-url http://pypi.douban.com/simple --trusted-host pypi.douban.com

ENV PYTHONPATH=$PYTHONPATH:/data/iflearner-flow/python
ENV FLOW_FEDERATE_CONF_PATH=/data/iflearner-flow/python/iflearner_flow_federate/conf/flow_federate_prod.yaml

WORKDIR /data/iflearner-flow/python/iflearner_flow_federate

CMD python3 app.py