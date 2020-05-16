# 基础镜像：python3.8镜像
FROM docker.io/python:3.8

# 镜像维护者的姓名和邮箱地址
MAINTAINER swd  <736202234@qq.com>

#开启50000端口
EXPOSE 50000

#添加本地文件到镜像中
ADD ./Server /python

# 工作目录
WORKDIR /python

CMD ["python","Server.py"]


