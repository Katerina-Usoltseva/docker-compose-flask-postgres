FROM flask:latest
ADD ./app /home/app/
WORKDIR /home/app/
EXPOSE 5000
ENTRYPOINT ["python3", "app.py"]