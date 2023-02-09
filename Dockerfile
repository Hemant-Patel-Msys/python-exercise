#Use an official Python runtime as the base image
FROM python:3.9-alpine
#Working directory
WORKDIR /app
#Copy the current directory contents into the container
copy requirements.txt requirements.txt
#Install the required packages specified in requirements.txt
RUN pip install -r requirements.txt
#
COPY . .
#command to run the application
#CMD ["python3","main.py","0.0.0.0:5000"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]