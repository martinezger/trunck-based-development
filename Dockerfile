FROM python:3.11
RUN pip install flask
COPY  ./main.py .
ENTRYPOINT [ "flask", "--app", "main", "run","--host","0.0.0.0" ]