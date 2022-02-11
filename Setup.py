import os

os.system('apt-get update')
os.system('apt upgrade')
os.system('apt-get install -y python3-pip')
os.system('git submodule update --init --recursive')
os.system('pip3 install h8mail')
os.system('h8mail -g')
os.system('mv h8mail_config.ini ./Email/h8mail/')
os.system('pip3 install wget')
os.system('sudo pip install json2html')
#Requirements installation
root = os.path.join('..', 'OSINT')
path = os.getcwd()
for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        if(name == "requirements.txt"):
            os.chdir(directory)
            os.system('python3 -m pip install -r ' + name)
            os.chdir(path)
#Setup installation
for directory, subdir_list, file_list in os.walk(root):
    for name in file_list:
        if(name == "setup.py"):
            os.chdir(directory)
            os.system('python3 ' + name + ' install')
            os.chdir(path)
#os.system('pip3 install requests_futures')
#os.system('pip3 install torrequest')
