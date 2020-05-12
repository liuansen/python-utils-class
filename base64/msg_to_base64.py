# -*- coding:utf-8 -*-
# author：Anson
from __future__ import unicode_literals

import base64
import time
import csv


def str_data(filename, filename2, filename3):
    f2 = open(filename2, 'w', encoding='UTF-8')
    f3 = open(filename3, 'w',  encoding='UTF-8', newline='')
    csv_write = csv.writer(f3)
    with open(filename, 'r', encoding='UTF-8') as f:
        fileds = []
        for line in f:
            str_list = line.split()
            if len(str_list) < 1:
                f2.write('\n')
                csv_write.writerow(fileds)
                print(fileds)
                fileds = []
                continue
            if str_list[0] == 't_join_result_ext.attack_time':
                data_sj = time.localtime(int(str_list[1][:10]))
                time_str = time.strftime("%Y-%m-%d %H:%M:%S",data_sj) 
                ss3 = "t_join_result_ext.attack_time" + "            " + time_str + '\n'
                f2.write(ss3) 
                fileds.append(time_str)
            
            elif str_list[0] == 't_join_result_ext.sip_ipv4':
                if len(str_list) == 1:
                    str_2 = ''
                else:
                    str_2 = str_list[1]
                fileds.append(str_2)

            elif str_list[0] == 't_join_result_ext.dip_ipv4':
                if len(str_list) == 1:
                    str_3 = ''
                else:
                    str_3 = str_list[1]
                fileds.append(str_3)

            elif str_list[0] == 't_join_result_ext.xff':
                if len(str_list) == 1:
                    str_4 = ''
                else:
                    str_4 = str_list[1] 
                fileds.append(str_4)
            
            elif str_list[0] == 't_join_result_ext.alarm_attack_type':
                if len(str_list) == 1:
                    str_5 = ''
                else:
                    str_5 = str_list[1] 
                fileds.append(str_5)

            elif str_list[0] == 't_join_result_ext.request':
                str_request = base64.b64decode(str_list[1]).decode("utf-8")
                ss1 = "t_join_result_ext.request" + "                " + str_request + '\n'
                f2.write(ss1)

            elif str_list[0] == 't_join_result_ext.response':
                str_response = base64.b64decode(str_list[1]).decode("utf-8")
                ss2 = "t_join_result_ext.response" + "               " + str_response  + '\n'
                f2.write(ss2)

            elif str_list[0] == 't_join_result_ext.log_time':
                data_sj = time.localtime(int(str_list[1][:10]))
                time_str = time.strftime("%Y-%m-%d %H:%M:%S",data_sj) 
                ss4 = "t_join_result_ext.log_time" + "               " + time_str + '\n'
                f2.write(ss4)
            
            else:
                f2.write(line)
    f.close
    f2.close
    
    # with open(filename3, 'a',  encoding='UTF-8') as f3:
    #     wirte = csv.writer(f3)
    #     write.wirterow(fields)


if __name__ == '__main__':
    list_e = {
        'one': ['E:\\code\\python\\project\\python-utils-class\\base64\\score_50.txt', 'E:\\code\\python\\project\\python-utils-class\\base64\\score_50_2.log', 'E:\\code\\python\\project\\python-utils-class\\base64\\score_50.csv'],
        'two': ['E:\\code\\python\\project\\python-utils-class\\base64\\score_95.txt', 'E:\\code\\python\\project\\python-utils-class\\base64\\score_95_2.log', 'E:\\code\\python\\project\\python-utils-class\\base64\\score_95.csv']
    }
    for i in range(2):
        if i == 0:
            key = 'one'
        else:
            key = 'two'
        str1 = list_e[key][0]
        str2 = list_e[key][1]
        str3 = list_e[key][2]
        msg = str_data(str1, str2, str3)
    