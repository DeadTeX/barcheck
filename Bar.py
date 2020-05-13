import os
import time
print ("хех Еше не придумали,но вот тест версия...")
print("#")
time.sleep (1)
print("##")
time.sleep (1)
print("###")
time.sleep (1)
print("####")
time.sleep (1)
print("#####")
time.sleep (1)
print("####")
time.sleep (1)
print("###")
time.sleep (1)
print("##")
time.sleep (1)
print("#")
print("-_-")
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
def banner():
    print(".______        ___      .______        ______   ______    _______   _______ ")
    print("|   _  \      /   \     |   _  \      /      | /  __  \  |       \ |   ____|")
    print("|  |_)  |    /  ^  \    |  |_)  |    |  ,----'|  |  |  | |  .--.  ||  |__   ")
    print("|   _  <    /  /_\  \   |      /     |  |     |  |  |  | |  |  |  ||   __|  ")
    print("|  |_)  |  /  _____  \  |  |\  \----.|  `----.|  `--'  | |  '--'  ||  |____ ")
    print("|______/  /__/     \__\ | _| `._____| \______| \______/  |_______/ |_______|")
    print("")
    print("  ______  __    __   _______   ______  __  ___  _______ .______             ")
    print(" /      ||  |  |  | |   ____| /      ||  |/  / |   ____||   _  \            ")
    print("|  ,----'|  |__|  | |  |__   |  ,----'|  '  /  |  |__   |  |_)  |           ")
    print("|  |     |   __   | |   __|  |  |     |    <   |   __|  |      /            ")
    print("|  `----.|  |  |  | |  |____ |  `----.|  .  \  |  |____ |  |\  \----.       ")
    print(" \______||__|  |__| |_______| \______||__|\__\ |_______|| _| `._____|       ")
    print("                                                     @an0n6m and @denkus24                          для канала @DeadTX")
    print("")
    print("")
    print("")




def vvd():
    global aa,bb,dd,cc,ff,hh,jj,ll,gg,ii,kk,ee,mm
    code = input('Code: ')
    code_nombers = list(code)
    code_nomber = list(map(int,code_nombers))
    aa=code_nomber[0]
    bb=code_nomber[1]
    cc=code_nomber[2]
    dd=code_nomber[3]
    ee=code_nomber[4]
    ff=code_nomber[5]
    gg=code_nomber[6]
    hh=code_nomber[7]
    ii=code_nomber[8]
    jj=code_nomber[9]
    kk=code_nomber[10]
    ll=code_nomber[11]
    mm=code_nomber[12]
    nch = 0
    ch = 0
    psl = 0
    prv = 0
    prvz = 0

def ppd():
    global prv
    ch = bb + dd + ff + hh + jj + ll
    #print(ch)
    #hj=input()
    ch = ch * 3
    nch = aa + cc + ee + gg + ii + kk
    psl = ch + nch
    #print(psl)
    #zx=input()
    prvz=psl%10
    #print(prvz)
    #xz=input()
    prv = 10 - prvz

def original():
    print("")
    print("")
    print("  ______   .______       __    _______  __  .__   __.      ___       __       ")
    print(" /  __  \  |   _  \     |  |  /  _____||  | |  \ |  |     /   \     |  |     ")
    print("|  |  |  | |  |_)  |    |  | |  |  __  |  | |   \|  |    /  ^  \    |  |     ")
    print("|  |  |  | |      /     |  | |  | |_ | |  | |  . `  |   /  /_\  \   |  |     ")
    print("|  `--'  | |  |\  \----.|  | |  |__| | |  | |  |\   |  /  _____  \  |  `----.")
    print(" \______/  | _| `._____||__|  \______| |__| |__| \__| /__/     \__\ |_______|")
    print("")
    print("")

def fake():
    print("")
    print("")
    print("  __       _        ")
    print(" / _| __ _| | _____ ")
    print("| |_ / _` | |/ / _ )")
    print("|  _| (_| |   <  __/")
    print("|_|  \__,_|_|\_\___|")
    print("")
    print("")

while True:
    cls()
    banner()
    vvd()
    ppd()

    if prv == mm:
        original()
        #print("оригинал")
    else:
        fake()
        #print("подделка")

    fin=input()
