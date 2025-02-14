arr=['ABCQ','B[4]R','CCDA','BT[15]']
def get_find(text):
    if text.find('[') == -1:
        return""
    start=text.find('[')+1
    end = text.find(']')
    return text[start:end]

for text in arr:
    ret=get_find(text)
    if ret:
        print(ret,end=" ")




