## ProxyPool

### 1.配置

#### 安装依赖
```
pip3 install pymysql
pip3 install requests
pip3 install bs4
pip3 install lxml
pip3 install sqlalchemy
```

#### 数据库配置
在`conf/setting.py`中配置数据库
```
DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/proxypool?charset=utf8'
```

初始化数据库
```
python3 init.py
```


### 2.运行
抓取代理IP
```
python3 proxypool.py
```

定时验证IP
```
python3 verify.py
```

### 3.启用HTTP Server
感谢 <a href="https://github.com/luzzbob">Luzz</a>

```
python3 server.py
curl http://localhost:5000/
```





