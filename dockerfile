FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt
CMD python3 step4_integrate_both.py