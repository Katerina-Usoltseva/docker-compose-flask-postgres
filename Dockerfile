FROM flask:latest
ADD ./app /home/app/
WORKDIR /home/app/
EXPOSE 5000
CMD ["python3", "app.py"]