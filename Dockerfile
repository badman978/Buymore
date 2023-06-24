FROM python:3.10.6
WORKDIR /BuyMore
RUN pip3 install fastapi uvicorn
COPY ./requirements.txt /BuyMore/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /BuyMore/requirements.txt
COPY ./app /BuyMore/app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]