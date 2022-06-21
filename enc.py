import random
import sys
import os
import logging



logging.basicConfig(level=logging.INFO)

__banner__="""\033[31m
\n [AKU SANGE TEMENIN DONG
╭━━╮╱╱╱╱╱╱╱╱╭━╮
┃╭╮┣━━┳━┳━┳┳┫━┫
┃┣┫┃┃┃┃╋┃╋┃┃┣━┃
╰╯╰┻┻┻┻━╋╮┣━┻━╯
╱╱╱╱╱╱╱╱╰━╯
]"""

__usage__="""\033[31m
COMMANDS : python enc.py file.py 'string'
╭━━╮╱╱╱╱╱╱╱╱╭━╮
┃╭╮┣━━┳━┳━┳┳┫━┫
┃┣┫┃┃┃┃╋┃╋┃┃┣━┃
╰╯╰┻┻┻┻━╋╮┣━┻━╯
╱╱╱╱╱╱╱╱╰━╯
"""

def main(files,string):
        s=open(files).read()
        z=[]
        for i in s:
                z.append(ord(i))
        pea=[]
        for i in z:
                pea.append(string.replace("'","").replace('"','')*i)
        file="""# vscode
# coding=utf-8
# ======================================= #
# HAPUS CREDIT GUA EBOL LU                #
# COMPILE BY AMOGUS                       #
# SUSAH DI DECODE YAK DECK MAMPUS         #
# 4M0GU2 ON TOP                           #
# ======================================= #
#╭━━╮╱╱╱╱╱╱╱╱╭━╮#
#┃╭╮┣━━┳━┳━┳┳┫━┫#
#┃┣┫┃┃┃┃╋┃╋┃┃┣━┃#
#╰╯╰┻┻┻┻━╋╮┣━┻━╯#
#╱╱╱╱╱╱╱╱╰━╯     #
amogus={};exec("".join([chr(len(i)) for i in amogus]))""".format(pea)
        open(files.replace(".py","-amogus.py"),"w").write(file)
        logging.info(" File Hass Been Saved > "+files.replace(".py","-amogus.py"))
        print("\033[0m")
try:
        print(__banner__)
        print("\033[34m")
        logging.info(" Amogus Berhasil Meng Compile > "+sys.argv[1]+" ")
        main(sys.argv[1],sys.argv[2])
except:
        print(__usage__)