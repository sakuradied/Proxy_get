#-*- coding=utf-8 -*-
#/usr/bin/python3
import requests
from urllib import request, error, parse
import re
import time
def about():
    print(
    r"""
    #####################################################
    #           _  http://sakuradied.com_ _           _ #
    # ___  __ _| | ___   _ _ __ __ _  __| (_) ___  __| |#
    #/ __|/ _` | |/ / | | | '__/ _` |/ _` | |/ _ \/ _` |#
    #\__ \ (_| |   <| |_| | | | (_| | (_| | |  __/ (_| |#
    #|___/\__,_|_|\_\\__,_|_|  \__,_|\__,_|_|\___|\__,_|#
    #####################################################
    本软件由sakuradied开发编写
    警告:
    本工具禁止一切形式的商业用途
    免责声明：
    本工具仅限于安全研究与教学使用，用户使用本工具所造成的所有后果，由用户承担全部法律及连带责任！作者不承担任何法律及连带责任。
    当你下载或复制或传输或运行本软件时均视为同意该协议
    """)

def get_proxy(url, ip_r, port_r, type_r):
    # 通过输入的表达式来获取ip以及端口还有代理类型
        head = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML,  like Gecko) Chrome/18.0.1025.166  Safari/535.19'
        }
#    try:
        req = request.Request(url, headers=head)
        response = request.urlopen(req, timeout=12)
        get_hteml = response.read().decode('utf-8')
        iplist = re.findall(str(ip_r), str(get_hteml))
        print(iplist)
        # 通过输入正则抓取IP
        portlist = re.findall(str(port_r), str(get_hteml))
        print(portlist)
        # 通过输入正则抓取端口
        typelist = re.findall(str(type_r), str(get_hteml))
        print(typelist)
        # 通过输入正则抓取代理类型
        file_list = open("proxy_List.txt","a+")
        #将读取到的数据用标准格式写入到列表
        i = 0
        while len(iplist) > i:
            file_text = str(typelist[i])+r"://"+str(iplist[i])+":"+str(portlist[i])+"\n"
            i = i + 1
            file_list.write(str(file_text))
        return(iplist, portlist, typelist)
#    except Exception as err:
#        print("error:", err)
        # 返回错误信息


def get_url_value(url, ip_r, port_r, type_r, value_star, value_end, sleep):
    if value_star != "":
        if value_end != "":
            # 开始判断从何处开始运行
            while int(value_end) >= int(value_star):
                run_url = url + str(value_end)
                print(str(run_url))
                value_end = int(value_end) - 1
                print(get_proxy(run_url, ip_r, port_r, type_r))
                time.sleep(int(sleep))
        else:
            return(get_proxy(url, ip_r, port_r, type_r))
    else:
        return(get_proxy(url, ip_r, port_r, type_r))


def main():
    urls = input("请输入要爬取的网址:")
    ip_r = input("请输入IP抓取正则表达式:")
    port_r = input("请输入端口抓取正则表达式:")
    type_r = input("请输入代理类型抓取正则表达式:")
    print("输入help查看帮助")
    value_star = ""
    value_end = ""
    sleep = 10
    while True:
        shell = input("shell>>")
        if shell == "help":
            print(
                r"""
                #####################################################
                #          _   http://sakuradied.com_ _           _ #
                # ___  __ _| | ___   _ _ __ __ _  __| (_) ___  __| |#
                #/ __|/ _` | |/ / | | | '__/ _` |/ _` | |/ _ \/ _` |#
                #\__ \ (_| |   <| |_| | | | (_| | (_| | |  __/ (_| |#
                #|___/\__,_|_|\_\\__,_|_|  \__,_|\__,_|_|\___|\__,_ |#
                #####################################################
                help        获得帮助
                export      输出抓取到的数据
                restart     重新输入数值
                value       指定抓取页数(默认为当前页面)
                help_value  value详细用法
                sleep       输入每个页面抓取间隔(默认10秒)
                exit        退出
                about       输入软件相关信息以及详细说明
                """
            )
        elif shell == "export":
            proxylist = get_url_value(str(urls), str(ip_r), str(port_r), str(type_r), str(value_star), str(value_end), sleep)
            if proxylist != None:
                print("IPList>", proxylist[0])
                print("portList>", proxylist[1])
                print("typelist>", proxylist[2])
            else:
                print("结束:本次未返回数据")

        elif shell == "restart":
            main()
        elif shell == "value":
            value_star = input("输入help_value查看详细方法.\n请输入开始的页数:")
            value_end = input("输入help_value查看详细方法.\n请输入结束的页数:")

        elif shell == "sleep":
            sleep = input("输入每个页面抓取间隔(默认10秒):")
        elif shell == "help_value":
            print('''
            整数型
            自定义从一个范围内抓取数据,要求url参数结尾为不不包含页面参数
            如"http://xxx.xxx/1"应写为"http://xxx.xxx/"
            ''')
        elif shell == "about":
            about()
        elif shell == "exit":
            exit()
main()


# <td data-title="IP">(.*)</td>
# <td data-title="PORT">(.*)</td>
# <td data-title="类型">(.*)</td>

#<td>((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))</td>
#<td>(6553[0-5]|655[0-2]\\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{1,3}|\d)</td>
#<td>(SOCKET4|SOCKET5|HTTP|HTTPS)</td>
