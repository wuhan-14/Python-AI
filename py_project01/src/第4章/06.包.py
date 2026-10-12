import utils.my_fun

utils.my_fun.log_separator1()
utils.my_fun.log_separator2()

from utils import my_fun

my_fun.log_separator1()
my_fun.log_separator2()
my_fun.log_separator3()

#__init__中必须有__all__=[]
from utils import *

my_fun.log_separator1()
my_fun.log_separator4()

print(my_var.PI)
print(my_var.NAME)

# 相对路径: 从当前文件所在目录开始查找
from utils.my_fun import log_separator1, log_separator3

# 绝对路径: 从项目的根目录下开始查找
#from 第4章.utils.my_fun import log_separator1, log_separator3

log_separator1()
log_separator3()