FROM python:latest
COPY . .
RUN pip install -r requirements.txt
RUN jupyter notebook --generate-config
CMD [ "jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]