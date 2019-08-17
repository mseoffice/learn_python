# pathlib 模块，相关模块 os.path

import sys
import os
# 获取当前文件路径
value1 = os.path.dirname(__file__)
value2 = os.getcwd()
print(sys._getframe().f_lineno, value1)
print(sys._getframe().f_lineno, value2)
# 获取上层/上层目录
print(sys._getframe().f_lineno, os.path.dirname(os.path.dirname(os.getcwd())))
# 拼接路径
print(sys._getframe().f_lineno, os.path.join(os.path.dirname(os.getcwd()), "关注", "微信公众号", "【进击的", "Coder】"))

import pathlib
# 获取当前文件路径
value3 = pathlib.Path.cwd()
print(sys._getframe().f_lineno, value3)
# 获取上层/上层目录
print(sys._getframe().f_lineno, pathlib.Path.cwd().parent.parent)
# 获取上层目录
print(sys._getframe().f_lineno, pathlib.Path.cwd().parent)
# 拼接路径
parts = ["关注", "微信公众号", "【进击的", "Coder】"]
print(sys._getframe().f_lineno, pathlib.Path.cwd().parent.joinpath(*parts))
# 模块PurePath
# PurePath.match
# 判断一下当前文件路径是否有符合'*.py' 规则的文件
print(sys._getframe().f_lineno, pathlib.PurePath(__file__).match('*.py'))

# 验证PurePath是一个对象，而不是一个路径字符串
import os

os_path = os.path.dirname(__file__)
pure_path = pathlib.PurePath(__file__)
print(sys._getframe().f_lineno, os_path, type(os_path))
print(sys._getframe().f_lineno, pure_path, type(pure_path))
print(sys._getframe().f_lineno, pathlib.PurePath(__file__).match('*.py'))

# pathlib的用法汇总
# 基本用法
# Path.iterdir()　　# 遍历目录的子目录或者文件
#
# Path.is_dir()　　# 判断是否是目录
#
# Path.glob()　　# 过滤目录(返回生成器)
#
# Path.resolve()　　# 返回绝对路径
#
# Path.exists()　　# 判断路径是否存在
#
# Path.open()　　# 打开文件(支持with)
#
# Path.unlink()　　# 删除文件或目录(目录非空触发异常)
#
# 基本属性
# Path.parts　　# 分割路径 类似os.path.split(), 不过返回元组
#
# Path.drive　　# 返回驱动器名称
#
# Path.root　　# 返回路径的根目录
#
# Path.anchor　　# 自动判断返回drive或root
#
# Path.parents　　# 返回所有上级目录的列表
#
# 改变路径
# Path.with_name()　　# 更改路径名称, 更改最后一级路径名
#
# Path.with_suffix()　　# 更改路径后缀
#
# 拼接路径
# Path.joinpath()　　# 拼接路径
#
# Path.relative_to()　　# 计算相对路径
#
# 测试路径
# Path.match()　　# 测试路径是否符合pattern
#
# Path.is_dir()　　# 是否是文件
#
# Path.is_absolute()　　# 是否是绝对路径
#
# Path.is_reserved()　　# 是否是预留路径
#
# Path.exists()　　# 判断路径是否真实存在
#
# 其他方法
# Path.cwd()　　# 返回当前目录的路径对象
#
# Path.home()　　# 返回当前用户的home路径对象
#
# Path.stat()　　# 返回路径信息, 同os.stat()
#
# Path.chmod()　　# 更改路径权限, 类似os.chmod()
#
# Path.expanduser()　　# 展开~返回完整路径对象
#
# Path.mkdir()　　# 创建目录
#
# Path.rename()　　# 重命名路径
#
# Path.rglob()　　# 递归遍历所有子目录的文件