FROM senesence/centos7-starter:1.0

RUN pip3.9 install numpy
RUN pip3.9 install pandas
RUN pip3.9 install matplotlib

COPY . /home/libs/BackendManager
WORKDIR /home/libs/BackendManager
RUN pip3.9 install .

WORKDIR /home/user/

CMD ["bash"]