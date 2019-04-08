from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(targetHost, targetPort):
    """测试连接"""
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((targetHost, targetPort))
        connSkt.send('KINTest\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+] %d/tcp open'.format(targetPort))
        print('[+] ' + str(results))
    except:
        screenLock.acquire()
        print('[-] %d/tcp closed'.format(targetPort))
    finally:
        screenLock.release()
        connSkt.close()

def portScan(targetHost, targetPorts):
    """端口扫描"""
    try:
        targetIP = gethostbyname(targetHost)
    except:
        print("[-] Connot resolve '%s' : Unkown host".format(targetHost))
        return

    try:
        targetName = gethostbyaddr(targetIP)
        print("[+] Scan Results for: " + targetName[0])
    except:
        print("[+] Scan Result for: " + targetIP)

    setdefaulttimeout(1)
    for targetPort in targetPorts:
        t = Thread(target=connScan, args=(targetHost, int(targetPort)))
        t.start()

