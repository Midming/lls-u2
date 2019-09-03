import time,os,yaml
from selenium.common.exceptions import NoSuchElementException


def read_yaml(path):
    with open(path,encoding='utf-8') as f:
        content=yaml.load(f,Loader=yaml.FullLoader)
        return content
def url_join(*args):
    seq='/'
    url=''
    for i in args:
        i=str(i)
        url=url+i+'/'
    if url[-1]=='/':
        url=url[:-1]
    return url
def ele_input(ele,keys):
    ele.clear()
    ele.click()
    ele.send_keys(keys)
    time.sleep(0.3)

def read_interface(dict_url,interface):
    backend=dict_url['self']
    first_keys=dict_url.keys()
    version=dict_url['version']
    url=None

    if interface in first_keys:
        v=dict_url[interface]['self']
        if interface=='login':
            url=url_join(version,interface)
        elif 1:
            url=url_join(version,backend,interface)

    else:
        for i in dict_url.values():
            if interface in i:
                # interface_self=i[interface]
                up_key_self=i['self']
                url=url_join(version,backend,up_key_self,interface)
    return url


def is_ele_exist(driver,by):
    ele=None
    try:
        ele=driver.find_element(by[0],by[1])
    except NoSuchElementException:
        ele=False
    return ele
def time_stamp():
    t=time.localtime(time.time())
    s=time.strftime("%Y%m%d%H%M%S",t)
    return s

def save_xls(wb,*args,dir=None):
    extension=r'.xls'
    filename=''
    path=''
    for i in range(len(args)):
        filename=filename+args[i]
    if filename:
        filename=filename+extension
        if dir:
            path=os.path.join(dir,filename)
            wb.save(path)
    return path
def write_xls(sheet,content):
    keys = content.keys()
    keys = list(keys)
    people_num = len(content['姓名'])
    key_num = len(keys)
    for i in range(0, key_num):
        sheet.write(0, i, keys[i])
    for i in range(0, people_num):
        for j in range(0, key_num):
            sheet.write(i + 1, j, str(content[keys[j]][i]))
def transfer_location(dict_content):
    ['css selector', '[data-pup="ComSettlement"]']
    for k,v in dict_content.items():
        t=type(v)
        l=len(v)
        if t==str:
            dict_content[k]=['css selector','[data-pup={}]'.format(v)]
        if t==list and l==2:
            if v[0]=='css':
                v[0]='css selector'
    return dict_content


