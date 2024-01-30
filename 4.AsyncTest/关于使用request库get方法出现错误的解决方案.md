# 关于使用request库get方法出现错误的解决方案



## 一、错误情况概述：

### 1、初始代码：

```python
import requests
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

TOTAL_NUMBER = 100
BASE_URL = 'https://static4.scrape.cuiqingcai.com/detail/5'

start_time = time.time()
for _ in range(1, TOTAL_NUMBER + 1):
    logging.info('Scraping %s', BASE_URL)
    response = requests.get(BASE_URL, timeout=10, verify=True)

end_time = time.time()
logging.info('Total time: %s seconds', end_time - start_time)
```

### 2、输出报错：

> Error Connecting: **HTTPSConnectionPool**(host='static4.scrape.cuiqingcai.com', port=443): **Max retries exceeded with url**: /detail/5 (**Caused by SSLError**(SSLEOFError(8, '**EOF occurred in violation of protocol (_ssl.c:1129)**')))

### 3、错误分析：

> requests.exceptions.SSLError: HTTPS连接池（主机='static4.scrape.cuiqingcai.com'，端口=443）：URL为/detail/5的最大重试次数已超过（由SSLError（SSLEOFError（8，'违反协议的EOF发生（_ssl.c：1129）'））引起）



## 二、普遍方案：

下面的2种方案也许能解决问题，但是经过尝试，**并非所有情况都能有效解决问题**。

### 1、添加`Connection`参数：

在Headers里添加`Connection`参数，使其为`close`，因为默认为`keep-alive`。

```python
headers = {
	'Connection': 'close' # 设置为关闭长连接
}
```

### 2、使用`request.session（）`的请求方式。

```python
s = requests.session()
s.keep_alive = False  # 关闭多余连接
s.get(url='xxx', headers='xxx', data='xxx)
```

下面给出更加全面和细致的解决方案。



## 三、个性解决方案：

### 1、错误问题分析：

### 2、个性解决方案：





























































































































































































