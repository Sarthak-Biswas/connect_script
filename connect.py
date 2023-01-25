import os
import requests

check_uri = "http://connectivitycheck.gstatic.com"

res = requests.head(url=check_uri)
os.system('nmcli radio wifi off')

captive_portal = None

if 'Location' in res.headers:
    captive_portal = res.headers['Location']
else:
    print("already connected")
    exit()


Headers = {'HOST': 'iit-p-ise-acs-02.iitp.ac.in:8443', 'Sec-Ch-Ua':'" Not A;Brand";v="99", "Chromium";v="96"', 'Sec-Ch-Ua-Mobile': '?0', 'Sec-Ch-Ua-Platform': '"Linux"', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Sec-Fetch-Site': 'none', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1', 'Sec-Fetch-Dest': 'document', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8', 'Connection': 'close'}

p1 = captive_portal.replace("gateway","PortalSetup.action")
print(captive_portal)
connect_portal = requests.get(p1,headers=Headers)
print("\n")


cookie = connect_portal.cookies.get_dict()
asid = cookie['APPSESSIONID']
sid = cookie['portalSessionId']
token = connect_portal.headers['token']
print(token)
print(asid)
print(sid)

bodi = {
    'token': token,
    'portal': '22483910-82dd-11e5-9e1e-74a2e6a350fe',
    'user.username': 'sarthak_2001cs61',
    'user.password': 'hcsnG5MU'
}

cook = {
    'APPSESSIONID': asid,
    'portalSessionId': sid,
    'checkCookiesEnabled': 'value'
}

p2 = "https://IIT-P-ISE-ACS-02.iitp.ac.in:8443/portal/LoginSubmit.action?from=LOGIN"

login = requests.post(p2,data=bodi,cookies=cook)

print(login.status_code)

p3 = "https://IIT-P-ISE-ACS-02.iitp.ac.in:8443/portal/Continue.action?from=POST_ACCESS_BANNER"

b2 = {'token': token}

cont = requests.post(p3,data=b2,cookies=cook)

print(cont)

p4 = "https://IIT-P-ISE-ACS-02.iitp.ac.in:8443/portal/DoCoA.action"

b3 = {
    'delayToCoA': '0',
    'coaType': 'Reauth',
    'waitForCoA': 'true',
    'portalSessionId': sid,
    'token': token
}

act = requests.post(p4,data=b3,cookies=cook)

print(act)
