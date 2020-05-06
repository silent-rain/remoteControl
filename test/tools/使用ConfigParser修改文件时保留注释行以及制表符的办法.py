import random
import re


def Repla_list_Notes(File, Old_list, New_list):  # 定义修改 # 号的函数，这么做的目的是为了使在使用ConfigParser的set时不把注释行去掉
    fopen = open(File, 'r')
    w_str = ""
    for line in fopen:
        if re.search(Old_list, line):
            line = re.sub(Old_list, str(random.random()) + New_list, line)  # str(random.random())：随机的0-1的小数并转换为字符串
            w_str += line
        else:
            w_str += line
    wopen = open(File, 'w')
    wopen.write(w_str)
    fopen.close()
    wopen.close()
    return


def Repla_list_Notes1(File, Old_list, New_list):  # 定义将 # 号修改回来的函数
    fopen = open(File, 'r')
    w_str = ""
    for line in fopen:
        if re.search(Old_list, line):
            line = re.sub(Old_list, New_list, line)
            w_str += line
        else:
            w_str += line
    wopen = open(File, 'w')
    wopen.write(w_str)
    fopen.close()
    wopen.close()
    return


with open(smbfile, 'r+') as file_insert_1:
    content = file_insert_1.read()
    file_insert_1.seek(0, 0)
    file_insert_1.write('[aba1注释1aba]\n' + content)  # 这一段就是在文件的第一行插入 [aba1注释1aba]

Repla_list_Notes(smbfile, '^#',
                 "aba1注释1aba = ")  # 将文件中 # 号 修改为 随机数aba1注释1aba = ，这么做的目的是为了使在使用ConfigParser的set时不把注释行去掉 ############################             cfgParser1 = ConfigParser() cfgParser1.read(smbfile)  #读取配置文件，直接读取ini文件内容  PathJur_r = (cfgParser1.get(MountDir_name, "valid users")) #获取变量 MountDir_name 中"valid users" 的值，返回为string类型

List_PathJur_r = PathJur_r.strip(',').split(',')
# 将PathJur_r 以 , 为分隔转换为列表 if Share_User not in List_PathJur_r:       cfgParser1.set(MountDir_name,'valid users',PathJur_r+','+Share_User)  #修改 valid users 的值为 PathJur+','+ddd     cfgParser1.write(open(smbfile,"w"))  #将修改写入 smbfile 中     print ('已增加',Share_User,'用户对共享',MountDir_name,'的读权限')
