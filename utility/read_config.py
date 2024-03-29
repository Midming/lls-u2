import yaml,os,time
import xlwt
from utility.basePage import BasePage
from urllib.parse import urljoin
from utility.utilities import read_yaml
from utility.utilities import url_join,read_interface,save_xls,time_stamp,write_xls,transfer_location,transfer_importBill_toList
from config.path import current_env_path,url_path,read_yaml,location_dir,dir_path
path_location_agency=os.path.join(location_dir,'agency')
path_location_platform=os.path.join(location_dir,'platform')
path_location_company=os.path.join(location_dir,'company')

path_project=os.path.dirname(dir_path)
path_test_data=os.path.join(path_project,'test_data')
path_test_file=os.path.join(path_test_data,'test_file')
path_test_file_temp= os.path.join(path_test_data, 'temp.yaml')


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
        self.angency=self.env['angency']
        self.company = self.env['company']
        self.urls=read_yaml(url_path)
        self.test_data=self.read_test_data()

    # def location_login(self,path=login_path):
    #     return read_yaml(path)
    @staticmethod
    def read_test_data():
        content=read_yaml(path_test_file_temp)
        return content
    def read_pt_import_bill(self):
        content = self.test_data['part-time-bill']
        content=transfer_importBill_toList(content)
        return content

    def get_bill_part_time(self,dict_content):
        content=dict_content
        wb=xlwt.Workbook()
        sheet=wb.add_sheet('工作表1',cell_overwrite_ok=True)
        expect = content.pop('expect')
        prefix=content.pop('prefix')
        write_xls(sheet,content)

        # keys = content.keys()
        # keys = list(keys)
        # people_num=len(content['姓名'])
        # key_num=len(keys)
        # for i in range(0,key_num):
        #     sheet.write(0,i,keys[i])
        # for i in range(0,people_num):
        #     for j in range(0,key_num):
        #         sheet.write(i+1,j,str(content[keys[j]][i]))
        t=time_stamp()
        time.sleep(1)
        filepath=save_xls(wb,prefix,t,dir=path_test_file)
        return filepath,expect






    def get_bill_full_time(self):
        pass

    def read_location_platform_login(self):
        self.path = os.path.join(path_location_platform, 'login.yaml')
        content = read_yaml(self.path)
        content=transfer_location(content)

        return content


    def read_location_company_login(self):
        self.path=os.path.join(path_location_company,'login.yaml')
        content = read_yaml(self.path)
        content=transfer_location(content)
        return content

    def read_location_company_dashboard(self):
        self.path=os.path.join(path_location_company,'dashboard.yaml')
        content=read_yaml(self.path)
        content=transfer_location(content)
        return content

    def read_location_company_billImport(self):
        self.path=os.path.join(path_location_company,'bill-import.yaml')
        content = read_yaml(self.path)
        content=transfer_location(content)

        return content

    def read_location_company_settlementDetails(self):
        self.path = os.path.join(path_location_company, 'settlement-details.yaml')
        content = read_yaml(self.path)
        content = transfer_location(content)

        return content

    def read_location_agency_dashboard(self):
        self.path=os.path.join(path_location_agency,'dashboard.yaml')
        content=read_yaml(self.path)
        content=transfer_location(content)

        return content

    def read_location_agency_login(self):
        self.path = os.path.join(path_location_agency, 'login.yaml')
        content = read_yaml(self.path)
        content=transfer_location(content)
        return content
    def read_location_agency_settlementRecord(self):
        path= os.path.join(path_location_agency, 'settlement_record.yaml')
        content = read_yaml(path)
        content = transfer_location(content)
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
#
# r=Read_config()
# #
# d=r.read_pt_import_bill()
# print(d)
# for i in d:
#     f=r.get_bill_part_time(i)
#     print(f)





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







