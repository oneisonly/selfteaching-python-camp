from collections import Counter


def stats_text_en(text,count):
   
    A=text.split()   
    B=[]   
    C=',.*-!'

    for AA in A:  
        for CC in C:  
            AA=AA.replace(CC,'') 
        if len(AA) and AA.isascii():   #用str型的isascii方法判断是否是英文单词
            B.append(AA)
    return Counter(B).most_common(count)  #Counter是统计单词次数，most-common是统计出现次数最高的
  
 

def cn(text,count):
  
    cn_character=[]
    for character in text:
        if '\u4e00'<=character<='\u9fff':   #unicode中 中文 字符的范围
            cn_character.append(character)
    print(cn_character)
    print(text)
    return Counter(cn_character).most_common(count)

def stats_text(text,count):
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型%s' % type(text))
    '''
    合并 英文词频和 中文字频的结果
    '''
    return stats_text_en(text,count)+cn(text,count)




