FROM public.ecr.aws/lambda/python:3.11

COPY ["requirements.txt", "./"]
RUN pip install -r requirements.txt

COPY ["lambda_function.py", "./"]
COPY ["marvin_voice.tflite", "./"]

CMD ["lambda_function.lambda_handler"]
