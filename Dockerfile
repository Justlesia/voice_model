FROM public.ecr.aws/lambda/python:3.11

#RUN pip install pipenv
COPY ["requirements.txt", "./"]
RUN pip install -r requirements.txt

#COPY ["Pipfile", "Pipfile.lock", "./"]
#RUN pipenv install --deploy --system

COPY ["lambda_function.py", "./"]
COPY ["marvin_voice.tflite", "./"]

CMD ["lambda_function.lambda_handler"]
