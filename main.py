import requests
import base64
import json
# from wox import Wox,WoxApi

# class markdown(Wox):
def upload(path):
    with open('1.jpg','rb') as jpg:
        img=jpg.read()
    url='https://sm.ms/api/upload'
    data={"smfile":img}
    r=requests.post(url,files=data).json()
    code=r['code']
    if code=='success':
        # successed
        url=r['url']
    else:
        # failed
        message=r['msg']
        url=message
    # print(json)
    return url

def toBase(path):
    #todo:get extension type
    ext= path.split('.')[-1]
    with open(path,'rb') as f:
        jpg=f.read()
    jpgBase=base64.b64encode(jpg).decode('utf8')
    baseStr=f'data:image/{ext};base64,{jpgBase}'
    return baseStr

def query(key): # md b/u /abc.jpg
    key=key.split(' ')
    path=key[-1]
    mode=key[1]
    if mode=='b':
        result=toBase(path)
    elif mode=='u':
        result=upload(path)
    else:
        result='?'
    return result

