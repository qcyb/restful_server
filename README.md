# 系统简介
pppoe用户充值系统

## 环境
python3 + django 1 + docker

## 启动充值系统

```bash
$ cp  restful_server/docker/.restful_server.env  .
$ docker-compose build --no-cache
$ docker-compose up -d redis mysql
$ docker-compose up web

"# 本地验证:"
因为Dockerfile内定义了8000端口映射到docker内部的80端口,
浏览器访问 http://127.0.0.1:8000/
