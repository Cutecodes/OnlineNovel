# 数据库应用作业，使用mssql和python flask实现简单的小说网站
## 依赖安装：pip install -r requirements.txt
## 切换到project文件夹：cd project
## python run.py
## 路由表

Map([<Rule '/reader/readercenter' (POST, OPTIONS, HEAD, GET) -> reader.readercenter>,
 <Rule '/author/authorcenter' (POST, OPTIONS, HEAD, GET) -> author.authorcenter>,
 <Rule '/editor/editorcenter' (POST, OPTIONS, HEAD, GET) -> editor.editorcenter>,
 <Rule '/editor/editorcharge' (POST, OPTIONS, HEAD, GET) -> editor.editorcharge>,
 <Rule '/author/createnovel' (POST, OPTIONS, HEAD, GET) -> author.createnovel>,
 <Rule '/author/authornovel' (POST, OPTIONS, HEAD, GET) -> author.authornovel>,
 <Rule '/reader/subscribe' (POST, OPTIONS, HEAD, GET) -> reader.readerssubscribe>,
 <Rule '/reader/bookshelf' (POST, OPTIONS, HEAD, GET) -> reader.readerbookshelf>,
 <Rule '/reader/register' (POST, OPTIONS, HEAD, GET) -> reader.register>,
 <Rule '/author/register' (POST, OPTIONS, HEAD, GET) -> author.register>,
 <Rule '/reader/login' (POST, OPTIONS, HEAD, GET) -> reader.login>,
 <Rule '/author/login' (POST, OPTIONS, HEAD, GET) -> author.login>,
 <Rule '/editor/login' (POST, OPTIONS, HEAD, GET) -> editor.login>,
 <Rule '/admin/model' (OPTIONS, POST) -> admin.model>,
 <Rule '/admin/login' (POST, OPTIONS, HEAD, GET) -> admin.admin_login>,
 <Rule '/author/' (POST, OPTIONS, HEAD, GET) -> author.index>,
 <Rule '/editor/' (POST, OPTIONS, HEAD, GET) -> editor.index>,
 <Rule '/search' (POST, OPTIONS, HEAD, GET) -> index.search>,
 <Rule '/admin/' (OPTIONS, HEAD, GET) -> admin.admin>,
 <Rule '/' (POST, OPTIONS, HEAD, GET) -> index.index>,
 <Rule '/author/<novel_id>/createchapter' (POST, OPTIONS, HEAD, GET) -> author.createchapter>,
 <Rule '/author/<novel_id>/<chapternum>' (POST, OPTIONS, HEAD, GET) -> author.updatechapter>,
 <Rule '/editor/<novelid>/<chapternum>' (POST, OPTIONS, HEAD, GET) -> editor.chargechapter>,
 <Rule '/author/<novel_id>' (POST, OPTIONS, HEAD, GET) -> author.authorchapter>,
 <Rule '/static/<filename>' (OPTIONS, HEAD, GET) -> static>,
 <Rule '/<novelid>/addbookshelf' (POST, OPTIONS, HEAD, GET) -> index.addbookshelf>,
 <Rule '/<novelid>/cover' (POST, OPTIONS, HEAD, GET) -> index.novelcover>,
 <Rule '/<novelid>/<chapternum>/subscribe' (POST, OPTIONS, HEAD, GET) -> index.subcribe>,
 <Rule '/<novelid>/<chapternum>' (POST, OPTIONS, HEAD, GET) -> index.chapter>,
 <Rule '/<novelid>' (POST, OPTIONS, HEAD, GET) -> index.novel>])
