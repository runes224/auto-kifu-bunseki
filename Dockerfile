FROM python:3.10.2
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
# RUN apt-get install build-essential 
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install numpy
RUN pip install cython
RUN pip install python-shogi
RUN pip install flask
RUN pip install requests
RUN ls -l /usr/bin/gcc
# RUN pip install ipywidgets
WORKDIR /app

COPY . /app

# RUN pip install /app/cshogi

CMD ["ls","-l", "/usr/bin/gcc"]
# CMD ["python","/app/app.py"]

# RUN python -m pip install cshogi