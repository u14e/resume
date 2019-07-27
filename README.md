## "阅后即焚" 在线简历

1. 用户访问 `resume/`, 填写邮箱申请短链接
2. 用户通过邮件里面的短链接地址访问在线简历(只能访问一次)

## 开发

```bash
mkvirtualenv resume
# windows 平台先 pip install win-packages/mysqlclient-1.4.2-cp36-cp36m-win_amd64.whl
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

cp .env_tpl .env
cp info_tpl.json info.json

# 启动服务
python manage.py runserver
```


## 参考链接:

- https://materializecss.com/
- https://github.com/mozillazg/ShortURL
- http://code.activestate.com/recipes/576918/
- https://github.com/Lxxyx/LxxyxResume