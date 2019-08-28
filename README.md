### 项目目录
- config：配置文件
    - environment(环境文件)：存储登陆账号、host
    - location(元素定位)：存储页面元素的定位方式
    - url：存储url
    - path：存储文件路径
- page：读取location文件中的元素定位方式来定位文件，存储页面元素对象
- test_dir 测试用例
- test_report 存储测试报告
- utility：辅助方法，读取文件方法等
- conftest.py 执行测试前的setup

### 运行
在终端执行  pytest filePath  
filePath为test_dir目录下的文件路径

### 目前完成
- 大管理后台和人力公司后台的登陆以及登陆后弹窗的处理



 

