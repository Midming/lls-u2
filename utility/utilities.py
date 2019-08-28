import time
from selenium.common.exceptions import NoSuchElementException
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
