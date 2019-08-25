import os,yaml
def read_yaml(path):
    with open(path,encoding='utf-8') as f:
        content=yaml.load(f,Loader=yaml.FullLoader)
        return content
current_path=os.path.realpath(__file__)
dir_path=os.path.dirname(current_path)
env_dir=os.path.join(dir_path,'environment')
env_path=os.path.join(env_dir,'env.yaml')
env=read_yaml(env_path)['env']
env_file=env+r'.yaml'
current_env_path=os.path.join(env_dir,env_file)

location_dir=os.path.join(dir_path,'location')
login_path=os.path.join(location_dir,'login')

url_path=os.path.join(dir_path,'url.yaml')
