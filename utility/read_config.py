import yaml,os
from utility.basePage import BasePage
from urllib.parse import urljoin
from utility.utilities import url_join,read_interface
from config.path import current_env_path,url_path,read_yaml,login_path


# current_path=os.path.realpath(__file__)
# father_path=os.path.dirname(current_path)
# grandfather_path=os.path.dirname(father_path)
# config_path=os.path.join(grandfather_path,'config')
# location_path=os.path.join(config_path,'location')
# login_path=os.path.join(location_path,'login.yaml')
# url_path=os.path.join(config_path,'url.yaml')
# env_path=os.path.join(config_path,'env')
# environment_path=os.path.join(env_path,'environment.yaml')
# def read_yaml(path):
#     with open(path,encoding='utf-8') as f:
#         content=yaml.load(f,Loader=yaml.FullLoader)
#         return content
#
# current_env=read_yaml(environment_path)['env']
# current_env=current_env+r'.yaml'
# current_env_path=os.path.join(env_path,current_env)

class Read_config:
    def __init__(self):
        self.env = self.read_current_env()
        self.platform = self.env['platform']
        self.host = self.platform['host']
        self.urls=read_yaml(url_path)

    def location_login(self,path=login_path):
        return read_yaml(path)

    def read_current_env(self,path=current_env_path):
        current_env=read_yaml(path)
        return current_env

    def platform_url(self,interface):
        dict_url=self.urls['platform']
        interface_url=read_interface(dict_url,interface)
        url=url_join(self.host,interface_url)
        return url


    def platform_role(self,role):
        roles=self.platform['role']
        r=roles[role]
        return r








# class Read_url():
#     def __init__(self):
#         self.config=Read_config()
#         self.env=self.config.read_current_env()
#         self.env_platform=self.env['platform']
#         self.host=self.env_platform['host']
#         # self.common_platform=self.config.url()['platform']
#     def platform(self,interface):
#         urls=self.config.url()['platform']
#         version=None
#         first_interfaces=None
#         temp=None
#         url=None
#         if 'version' in urls.keys():
#             version=urls.pop('version')
#             first_interfaces=list(urls.keys())
#             if interface in first_interfaces:
#                 temp=urls[interface]['self']
#                 url=url_join(self.host,version,temp)
#             elif 1:
#                 for i in urls.values():
#                     if interface in i:
#                         temp=i[interface]
#                         first_interface=i['self']
#                         url=url_join(self.host,version,first_interface,temp)
#             return url











# r=Read_config()
# e=r.read_current_env()
# print(e)
# r_url=Read_url()
# r1=r_url.platform_login()
# print(r1)







