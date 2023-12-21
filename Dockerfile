FROM python

ENV TZ="Asia/Singapore"
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /
RUN mkdir -p staycation/app
COPY app /staycation/app
COPY requirements.txt /staycation

# WORKDIR /staycation/app
WORKDIR /staycation
RUN pip3 install -r requirements.txt --no-cache-dir 
RUN pip3 install gunicorn --no-cache-dir && \
    pip3 install Werkzeug==2.2.2 --no-cache-dir 
    # wget -qO - https://www.mongodb.org/static/pgp/server-7.0.asc | apt-key add - && \
    # echo 'deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse' | tee -a /etc/apt/sources.list.d/mongodb-org-7.0.list && \
    # apt update && \
    # apt install mongodb-org -y

WORKDIR /staycation
# # ENV PYTHONPATH=/staycation/app
# ENV PYTHONPATH=/staycation

# EXPOSE 5000
# # CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-m", "007", "app:app"]
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-m", "007", "app:create_app()"]