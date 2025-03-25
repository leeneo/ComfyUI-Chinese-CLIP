def Cn2EnCode(text):
    CnText = u'，。！？【】（）《》“‘、￥——'
    EnText = u',.!?[]()<>"\'\\$-'
    table= {ord(f):ord(t) for f,t in zip(CnText,EnText)}
    return text.translate(table)


# print(Cn2EnCode('，。！？【】（）《》“‘、￥——'))
