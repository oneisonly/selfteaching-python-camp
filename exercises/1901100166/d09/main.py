from mymodule import stats_word  #从m文件中导入st模块
from os import path #os库里带的一个path模块
import json
import re 
import logging  #这是两种方法

logging.basicConfig(
    format='file:%(filename)s|line:%(lineno)d|message:%(message)s',level=logging.DEBUG)

def load_file():
    
    file_path=path.join(path.dirname(path.abspath(__file__)),'tang300.json') #__file__魔法字符串表示当前文件名
    #abspath是获得当前文件的绝对路径，dirname目录名
    print('当前路径:',__file__,'\n读取文件路径：',file_path)

    with open(file_path, 'r',encoding='utf-8') as f:  
        #这一步是读取文件 open是一个内置数，utf-8是编码，encoding是读取模式
        return f.read()

def merge_poems(data):
    poems=''
    for item in data:
        poems += item.get('contents','')
    return poems

def main():
    try:
        data=load_file()
        logging.info(data)  #0表示第一个字符
        poems=merge_poems(json.loads(data))
        logging.info('result==>%s',stats_word.cn(poems,100))
    except Exception as e:
        logging.exception(e)

if __name__ == "__main__":
    main()
    
      