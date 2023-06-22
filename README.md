[<img alt="LOGO" src="http://www.gqylpy.com/static/img/favicon.ico" height="21" width="21"/>](http://www.gqylpy.com)
[![Release](https://img.shields.io/github/release/gqylpy/celeste.svg?style=flat-square")](https://github.com/gqylpy/celeste/releases/latest)
[![Python Versions](https://img.shields.io/pypi/pyversions/celeste)](https://pypi.org/project/celeste)
[![License](https://img.shields.io/pypi/l/celeste)](https://github.com/gqylpy/celeste/blob/main/LICENSE)

# celeste

> 创建蓝图以定义数据结构，使用蓝图以验证数据。

<kbd>pip3 install celeste</kbd>

```python
from celeste import Celeste

celeste = Celeste({'name': {type: str}})
celeste.validate({'name': 'Tom'})
```
