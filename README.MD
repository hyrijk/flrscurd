- 安装依赖库
```
pip install -r requirement.txt
```
- 直接运行
```
python app.py
```

- gunicorn 部署(Linux环境)
  - 安装 gunicorn
  ```
  pip install gunicorn
  ```
  - 运行
  ```
  gunicorn app:app -b 0.0.0.0:5000 -D
  ```
- 测试  
使用 [`curl`](http://www.ruanyifeng.com/blog/2011/09/curl.html) 发送http请求
  - 添加文章
  ```
  curl -i -X POST 127.0.0.1:5000/articles -d "{\"title\": \"this is title\", \"author\": \"this is author\", \"content\": \"this is content\"}"  -H "Content-Type:application/json"
  ```
  ```
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 148
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Headers: Content-Type,Authorization
    Access-Control-Allow-Methods: GET,PUT,POST,DELETE
    Server: Werkzeug/0.11.9 Python/3.5.0
    Date: Sat, 08 Oct 2016 08:10:02 GMT

    {
      "author": "this is author",
      "content": "this is content",
      "id": 1,
      "link": "http://127.0.0.1:5000/article/1",
      "title": "this is title"
    }
  ```

  - 获取所有文章
  ```
  curl -i 127.0.0.1:5000/articles
  ```
  ```
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 20
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Headers: Content-Type,Authorization
    Access-Control-Allow-Methods: GET,PUT,POST,DELETE
    Server: Werkzeug/0.11.9 Python/3.5.0
    Date: Sat, 08 Oct 2016 07:57:39 GMT

    {
      "articles": []
    }
  ```

  - 获取文章详情
  ```
  curl -i 127.0.0.1:5000/article/1
  ```
  ```
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 148
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Headers: Content-Type,Authorization
    Access-Control-Allow-Methods: GET,PUT,POST,DELETE
    Server: Werkzeug/0.11.9 Python/3.5.0
    Date: Sat, 08 Oct 2016 08:12:58 GMT

    {
      "author": "this is author",
      "content": "this is content",
      "id": 1,
      "link": "http://127.0.0.1:5000/article/1",
      "title": "this is tilte"
    }
  ```

  - 更新文章
  ```
  curl -i -X PUT 127.0.0.1:5000/article/1 -d "{\"title\": \"this is the modified title\"}"  -H "Content-Type:application/json"
  ```
  ```
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 161
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Headers: Content-Type,Authorization
    Access-Control-Allow-Methods: GET,PUT,POST,DELETE
    Server: Werkzeug/0.11.9 Python/3.5.0
    Date: Sat, 08 Oct 2016 08:18:23 GMT

    {
      "author": "this is author",
      "content": "this is content",
      "id": 1,
      "link": "http://127.0.0.1:5000/article/1",
      "title": "this is the modified title"
    }
  ```

  - 删除文章
  ```
  curl -i -X DELETE 127.0.0.1:5000/article/1
  ```
  ```
    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 43
    Access-Control-Allow-Origin: *
    Access-Control-Allow-Headers: Content-Type,Authorization
    Access-Control-Allow-Methods: GET,PUT,POST,DELETE
    Server: Werkzeug/0.11.9 Python/3.5.0
    Date: Sat, 08 Oct 2016 08:14:30 GMT

    {
      "message": "\u5220\u9664\u6210\u529f"
    }
  ```
