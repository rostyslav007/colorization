FROM python:3
LABEL maintainer roxa0706@gmail.com
RUN git clone -q https://github.com/rostyslav007/colorization
WORKDIR colorization
RUN  pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python3","app.py"]

