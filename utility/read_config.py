import yaml,os
import xlwt
from utility.basePage import BasePage
from urllib.parse import urljoin
from utility.utilities import url_join,read_interface,save_xlsx,time_stamp
from config.path import current_env_path,url_path,read_yaml,location_dir,dir_path
path_location_agency=os.path.join(location_dir,'agency')
path_location_platform=os.path.join(location_dir,'platform')
path_location_company=os.path.join(location_dir,'company')

path_project=os.path.dirname(dir_path)
path_test_data=os.path.join(path_project,'test_data')
path_test_file=os.path.join(path_test_data,'test_file')


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
def read_yaml(path):
    with open(path,encoding='utf-8') as f:
        content=yaml.load(f,Loader=yaml.FullLoader)
        return content

class Read_config:
    def __init__(self):
        self.env = self.read_current_env()
        self.platform = self.env['platform']
        self.angency=self.env['angency']
        self.company = self.env['company']
        self.urls=read_yaml(url_path)
        self.test_data=self.read_test_data()

    # def location_login(self,path=login_path):
    #     return read_yaml(path)
    @staticmethod
    def read_test_data():
        path=os.path.join(path_test_data,'temp.yaml')
        print(path)
        content=read_yaml(path)
        return content
    def get_bill_part_time(self):
        content=self.test_data['part-time-bill']
        wb=xlwt.Workbook()
        sheet=wb.add_sheet('工作表1',cell_overwrite_ok=True)

        prefix=content.pop('prefix')
        keys = content.keys()
        keys = list(keys)
        people_num=len(content['姓名'])
        key_num=len(keys)
        for i in range(0,key_num):
            sheet.write(0,i,keys[i])
        for i in range(1,people_num+1):
            for j in range(0,key_num):
                sheet.write(i+1,content[keys[j]][i+1])
        t=time_stamp()
        save_xlsx(wb,prefix,t,dir=path_test_file)





    def get_bill_full_time(self):
        pass

    def read_location_platform_login(self):
        self.path = os.path.join(path_location_platform, 'login.yaml')
        content = read_yaml(self.path)
        return content


    def read_location_company_login(self):
        self.path=os.path.join(path_location_company,'login.yaml')
        content = read_yaml(self.path)
        return content

    def read_location_company_dashboard(self):
        self.path=os.path.join(path_location_company,'dashboard.yaml')
        content=read_yaml(self.path)
        return content

    def read_location_company_billImport(self):
        self.path=os.path.join(path_location_company,'bill-import.yaml')
        content = read_yaml(self.path)
        return content

    def read_location_agency_dashboard(self):
        self.path=os.path.join(path_location_agency,'dashboard.yaml')
        content=read_yaml(self.path)
        return content

    def read_location_agency_login(self):
        self.path = os.path.join(path_location_agency, 'login.yaml')
        content = read_yaml(self.path)
        return content


    def read_current_env(self,path=current_env_path):
        current_env=read_yaml(path)
        return current_env

    def platform_url(self,interface):
        dict_url=self.urls['platform']
        interface_url=read_interface(dict_url,interface)
        url=url_join(self.platform['host'],interface_url)
        return url


    def platform_role(self,role):
        roles=self.platform['role']
        r=roles[role]
        return r


    def angency_url(self,interface):
        dict_url=self.urls['angency']
        interface_url = read_interface(dict_url, interface)
        url = url_join(self.angency['host'], interface_url)
        return url
    def company_url(self,interface):
        dict_url=self.urls['company']
        interface_url = read_interface(dict_url, interface)
        url = url_join(self.company['host'], interface_url)
        return url

    def angency_role(self,role):
        roles=self.angency['role']
        r=roles[role]
        return r
    def company_role(self,role):
        roles=self.company['role']
        r=roles[role]
        return r

r=Read_config()

c=r.get_bill_part_time()






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







