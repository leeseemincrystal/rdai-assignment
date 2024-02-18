# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip3 install -q datasets loralib sentencepiece
RUN pip3 -q install bitsandbytes accelerate xformers einops

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
#CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]