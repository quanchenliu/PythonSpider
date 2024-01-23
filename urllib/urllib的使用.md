# urllib的使用

`urllib`库包含4个模块：

- [ ] `request`模块：HTTP请求模块；
- [ ] `error`模块：异常处理模块；
- [ ] `parse`模块：一个URL处理的工具模块；
- [ ] `robotparser`模块：用来识别网页的robots.txt文件，然后判断哪些网页可以爬取。



## 一、request模块

**1、urlopen：**`urlopen(url, data, timeout)`

- `url`：定位要爬取的网页

- `data`：要提交给服务器的参数。默认为`None`，表示使用GET请求。如果提供了数据，将**使用POST请求**，数据需要是字节类型（`bytes`）

  ​			`data = bytes(urllib.parse.urlencode({'name':'germey'}), encoding = 'utf-8')`

- `timeout`：用于设置超时时间。

**2、Request：**利用 `urlopen` 方法可以发起最基本的请求，但往往需要在请求添加一些 `headers` 信息，这就需要使用 `Request` 类来构建请求。Request的构造方法如下：

​		`class urllib.request.Request(url, data, headers={}, origin_req_host, unverifiable, method)`

- url：用于请求URL，是**必传参数**；
- data：如果要使用这一参数，**必须是bytes类型**。如果数据是字典，可以先使用parse.urlencode方法进行编码；
- headers：一个字典，这就是请求头，最常见的方法就是添加**User-Agent**；
- origin_req_host：请求方的host名称或者IP地址；
- unverifiable：用于指明请求是否是无法验证的，默认值为False（用户没有足够的权限来接收这一请求的结果）；
- method：一个字符串，用于指示请求使用的方法。

**3、一些高级用法：**































