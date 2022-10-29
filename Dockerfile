FROM public.ecr.aws/lambda/python:3.8

# Copy function code
COPY app.py app.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.lambda_handler" ]