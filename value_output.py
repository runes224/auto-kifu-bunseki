import sys
import requests
from shogi import Engine


def listoutput():
    engine = Engine('/home/ec2-user/auto-kifu-bunseki/LesserkaiSrc/Lesserkai/Lesserkai')

    response = requests.get('https://www.shogi-extend.com/w.json?query=rentokomori&per=10')
    jsonData = response.json()
    kif = jsonData["records"][0]["sfen_body"]
    kifList = kif.split( )
    del kifList[0:7]

    # engine.setoption("MultiPV", "2")
    engine.isready()
    engine.usinewgame()
    # engine.position()
    # engine.go(listener=print)

    #out.txt初期化
    with open("out.txt", 'w') as f:
        f.truncate(0)


        j = []
        for i in kifList:
            j.append(i)
            engine.position(j)
            # engine.position(sfen='sfen 7nl/5kP2/3p2g1p/2p1gp3/p6sP/s1BGpN3/4nPSp1/1+r4R2/L1+p3K1L w GSNLPb6p 122')
            # engine.go()
            #ここから下はなんとかしたかったけど不明
            sys.stdout = open('out.txt', 'a')
            engine.go(listener=print)
        sys.stdout = sys.__stdout__ # 元に戻す
    return kif['moves']