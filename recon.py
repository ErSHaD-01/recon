
import os
import argparse
import re
import socket
os.system('cls')

# --- [ Check Library ] --- #
try :
    import requests
    print('(requests) library is installed')
except :
    os.system('pip install requests')
    os.system('cls')

try :
    from bs4 import BeautifulSoup
    print('(beautifulsoup4) library is installed')
except :
    os.system('pip install beautifulsoup4')
    os.system('cls')

try :
    from selenium import webdriver
    print('(webdriver) library is installed')
except :
    os.system('pip install -U selenium')
    os.system('cls')


try :
    import whois
    print('(whois) library is installed')
except :
    os.system('pip install python-whois')
    os.system('cls')

try :
    import wget
    print('(wget) library is installed')
except :
    os.system('pip install wget')
    os.system('cls')

try :
    from Wappalyzer import Wappalyzer, WebPage
    print('(Wappalyzer) library is installed')
except :
    os.system('pip install python-Wappalyzer')
    os.system('cls')    
# ------------------------- #


# --- [ args ] --- #
parser = argparse.ArgumentParser(description='Process some inputs.')
parser.add_argument('--url', type=str, help='Get url')
parser.add_argument('--tag', type=str, help='Get the desired tag')
parser.add_argument('--depth', type=int, help='Get depth url')
parser.add_argument('--subdomain', type=int, help='Find the subdomain (Burt Force)')
parser.add_argument('--ip_address', type=int, help='Get the ip address of the server')
parser.add_argument('--save_file', type=int, help='Save as a file')
args = parser.parse_args()
# ---------------- #

# --- [ Banner ] --- #
def banner() :
    print("""
╔═════════════════════════════════════════════════[ Recon-Dos ]═════════════════════════════════════════════════╗
╠ U3er => https://github.com/dead-u3er/Recon-Dos                                                                ║
╠ ErSHad => https://github.com/ErSHaD-01/Recon-Dos                                                              ║
╠ Version => 1.0                                                                                                ║
╠════════════════════════════════════════════════[ information ]════════════════════════════════════════════════╣
╠ python3 recon-dos.py --url <URL> --depth <depth URL> --sub <SUBDOMAIN> --ip  <IP_ADDRESS> --save <SAVE_FILE>  ║
║                                                                                                               ║
╠ <URL> => URL address of the target website                                                                    ║
║                                                                                                               ║
╠═╦═ <depth URL> => Number of depth of navigation in links [0,1,2]                                              ║
║ ╠══ 0 => False                                                                                                ║
║ ╠══ 1 => True - Find in input url                                                                             ║
╠═╩══ 2 => True - Find in input url and find in obtained url                                                    ║
║                                                                                                               ║
╠═╦═ <TAG> => Get the desired tag [0,1]                                                                         ║
║ ╠══ 0 => False                                                                                                ║
╠═╩══ 1 => True - depth                                                                                         ║
║                                                                                                               ║
╠═╦═ <SUBDOMAIN> => Some subdomain finds [0,1,2]                                                                ║
║ ╠══ 0 => False                                                                                                ║
║ ╠══ 1 => True                                                                                                 ║
╠═╩══ 2 => True - depth                                                                                         ║
║                                                                                                               ║
╠═╦═ <IP_ADDRESS> => Get the ip address of the server [0,1,2]                                                   ║
║ ╠══ 0 => False                                                                                                ║
║ ╠══ 1 => True                                                                                                 ║
╠═╩══ 2 => True - depth                                                                                         ║
║                                                                                                               ║
╠═╦═ <SAVE_FILE> => Save as a file [0,1,2]                                                                      ║
║ ╠══ 0 => False                                                                                                ║
║ ╠══ 1 => True - Save as TXT                                                                                   ║
║ ╠══ 2 => True - Save as CVS                                                                                   ║
║ ╠══ 3 => True - Save as HTML                                                                                  ║
╠═╩══ 4 => True - Save as SQL - Soon                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════════════════════════════════════════╝
    """)
# ------------------ #


links = []
links_depth = []
links_depth1 = []
# --- [ Edit Domain ] --- #
def domain_http(url):
    filter = True
    andis_domain = 0
    domain_edit = ""
    domain = ""

    if url.startswith("https://") :
        domain_edit = url.replace("https://","")
        if domain_edit.startswith("www."):
            domain_edit = domain_edit.replace("www." , "")
    elif url.startswith("http://") :
        domain_edit = url.replace("http://","")
        if domain_edit.startswith("www."):
            domain_edit = domain_edit.replace("www." , "")
    
    for i in range(0,len(domain_edit)) :
        if domain_edit[i] == "/" and filter :
            filter = False
            andis_domain = i
    
    if andis_domain == 0 :
        return domain_edit
    for i in range(0 , andis_domain) :
        domain += domain_edit[i]
    
    return domain
# ----------------------- #

# --- [ get tag response ] --- #
def get_url(url , tag):
    if args.depth == 1:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        for link in soup.find_all(str(tag)):
            if (tag == "a"):
                href = link.get("href")
                if href is not None and href.startswith("http"):
                    links.append(href)
            elif(tag == "img" or tag == "script" or tag == "video" or tag == "audio" or tag == "iframe"):
                src = link.get("src")
                if src is not None and src.startswith("http"):
                    links.append(src)
                else:
                    res_src = "https://" + domain_http(url)
                    res_src += str(src)
                    links.append(res_src)
    elif args.depth == 2:

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        for link in soup.find_all(str(tag)):
            if (tag == "a"):
                href = link.get("href")
                if href is not None and href.startswith("http"):
                    links.append(href)
            elif(tag == "img" or tag == "script" or "video" or "audio" or "iframe"):
                src = link.get("src")
                if src is not None and src.startswith("http"):
                    links.append(src)
                else:
                    res_src = "https://" + domain_http(url)
                    res_src += str(src)
                    links.append(res_src)
        for i in range(0 , len(links)):
            response_depth = requests.get(links[i])
            soup_depth = BeautifulSoup(response_depth.content , "html.parser")
            links_depth = []
            for link in soup_depth.find_all(str(tag)):
                if (tag == "a"):
                    href_depth = link.get("href")
                    if href_depth is not None and href_depth.startswith("http"):
                        links_depth.append(href_depth)
                elif (tag == "iframe"):
                    src_depth = link.get("src")
                    if src_depth is not None and src_depth.startswith("http"):
                        links_depth.append(src_depth)
                    else:
                        res_src_depth = "https://" + domain_http(url)
                        res_src_depth += src_depth
                        links_depth(res_src_depth)
            links_depth1.append(links_depth)

# ---------------------------- #

# --- [ Sub Domain ] --- #
def sub_domain(url):
            subs = []
            with open("word.txt", "r") as file: 
                    for line in file: 
                        subdomain_ = line.strip()
                        subdomain_ += "." + domain_http(url)
                        subs.append(subdomain_)                
            for j in range(0 , len(subs)):
                        try:
                            answers = socket.gethostbyname(subs[j])
                            return subs[j] + " - " + answers
                        except:
                            pass
# ---------------------- #

# --- [ Status Code ] --- #
def status_code(url) :
    response = requests.get(url)
    if response.status_code == 100:
        return "Continue"
    elif response.status_code == 101:
        return str(response.status_code) + " - Switching Protocols"
    elif response.status_code == 102:
        return str(response.status_code) + " - Processing"
    elif response.status_code == 103:
        return str(response.status_code) + " - Early Hints"
    elif response.status_code == 200:
        return str(response.status_code) + " - OK"
    elif response.status_code == 201:
        return str(response.status_code) + " - Created"
    elif response.status_code == 202:
        return str(response.status_code) + " - Accepted"
    elif response.status_code == 203:
        return str(response.status_code) + " - Non-Authoritative Information"
    elif response.status_code == 204:
        return str(response.status_code) + " - No Content"
    elif response.status_code == 205:
        return str(response.status_code) + " - Reset Content"
    elif response.status_code == 206:
        return str(response.status_code) + " - Partial Content"
    elif response.status_code == 207:
        return str(response.status_code) + " - Multi-Status"
    elif response.status_code == 208:
        return str(response.status_code) + " - Already Reported"
    elif response.status_code == 226:
        return str(response.status_code) + " - IM Used"
    elif response.status_code == 300:
        return str(response.status_code) + " - Multiple Choices"
    elif response.status_code == 301:
        return str(response.status_code) + " - Moved Permanently"
    elif response.status_code == 302:
        return str(response.status_code) + " - Found"
    elif response.status_code == 303:
        return str(response.status_code) + " - See Other"
    elif response.status_code == 304:
        return str(response.status_code) + " - Not Modified"
    elif response.status_code == 305:
        return str(response.status_code) + " - Use Proxy"
    elif response.status_code == 306:
        return str(response.status_code) + " - unused"
    elif response.status_code == 307:
        return str(response.status_code) + " - Temporary Redirect"
    elif response.status_code == 308:
        return str(response.status_code) + " - Permanent Redirect"
    elif response.status_code == 400:
        return str(response.status_code) + " - Bad Request"
    elif response.status_code == 401:
        return str(response.status_code) + " - Unauthorized"
    elif response.status_code == 402:
        return str(response.status_code) + " - Payment Required"
    elif response.status_code == 403:
        return str(response.status_code) + " - Forbidden"
    elif response.status_code == 404:
        return str(response.status_code) + " - Not Found"
    elif response.status_code == 405:
        return str(response.status_code) + " - Method Not Allowed"
    elif response.status_code == 406:
        return str(response.status_code) + " - Not Acceptable"
    elif response.status_code == 407:
        return str(response.status_code) + " - Proxy Authentication Required"
    elif response.status_code == 408:
        return str(response.status_code) + " - Request Timeout"
    elif response.status_code == 409:
        return str(response.status_code) + " - Conflict"
    elif response.status_code == 410:
        return str(response.status_code) + " - Gone"
    elif response.status_code == 411:
        return str(response.status_code) + " - Length Required"
    elif response.status_code == 412:
        return str(response.status_code) + " - Precondition Failed"
    elif response.status_code == 413:
        return str(response.status_code) + " - Payload Too Large"
    elif response.status_code == 414:
        return str(response.status_code) + " - URI Too Long"
    elif response.status_code == 415:
        return str(response.status_code) + " - Unsupported Media Type"
    elif response.status_code == 416:
        return str(response.status_code) + " - Range Not Satisfiable"
    elif response.status_code == 417:
        return str(response.status_code) + " - Expectation Failed"
    elif response.status_code == 418:
        return str(response.status_code) + " - I'm a teapot"
    elif response.status_code == 421:
        return str(response.status_code) + " - Misdirected Request"
    elif response.status_code == 422:
        return str(response.status_code) + " - Unprocessable Content"
    elif response.status_code == 423:
        return str(response.status_code) + " - Locked"
    elif response.status_code == 424:
        return str(response.status_code) + " - Failed Dependency"
    elif response.status_code == 425:
        return str(response.status_code) + " - Too Early"
    elif response.status_code == 426:
        return str(response.status_code) + " - Upgrade Required"
    elif response.status_code == 428:
        return str(response.status_code) + " - Precondition Required"
    elif response.status_code == 429:
        return str(response.status_code) + " - Too Many Requests"
    elif response.status_code == 431:
        return str(response.status_code) + " - Request Header Fields Too Large"
    elif response.status_code == 451:
        return str(response.status_code) + " - Unavailable For Legal Reasons"
    elif response.status_code == 500:
        return str(response.status_code) + " - Internal Server Error"
    elif response.status_code == 501:
        return str(response.status_code) + " - Not Implemented"
    elif response.status_code == 502:
        return str(response.status_code) + " - Bad Gateway"
    elif response.status_code == 503:
        return str(response.status_code) + " - Service Unavailable"
    elif response.status_code == 504:
        return str(response.status_code) + " - Gateway Timeout"
    elif response.status_code == 505:
        return str(response.status_code) + " - HTTP Version Not Supported"
    elif response.status_code == 506:
        return str(response.status_code) + " - Variant Also Negotiates"
    elif response.status_code == 507:
        return str(response.status_code) + " - Insufficient Storage"
    elif response.status_code == 508:
        return str(response.status_code) + " - Loop Detected"
    elif response.status_code == 510:
        return str(response.status_code) + " - Not Extended"
    elif response.status_code == 511:
        return str(response.status_code) + " - Network Authentication Required"
    else:
        return "Unknown status code:", str(response.status_code)
# ----------------------- #

# --- [ Title ] --- #
def title(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("title")
    return title
# ----------------- #

# --- [ IP ] --- #
def get_ip(url):
    domain = domain_http(url)
    ip_address = socket.gethostbyname(domain)
    return ip_address
# -------------- #

# --- [ PORT ] --- #
def port(ip):
        ports = []
        for i in range (79 , 82):
            ports.append(i)
        for port in ports:  
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((get_ip(ip), port))
            if result == 0:
                return "port " + str(port) + " is open"
            sock.close()
# -------------- #

# --- [ Regex ] --- #
def regex(url):
    info_email = []
    info_tel = []
    info_phone = []
    information = []
    text = requests.get(url).text
    pattern_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    pattern_phone = r"\b(?:\+)?09\d{9}\b"
    pattern_tel = r"\b[0-9]+\s*-\s*[0-9]{5,}\b"
        
    email = re.findall(pattern_email, text)
    if email:
        info_email.append(email)
    else:
        info_email.append("No email found")

    phone = re.findall(pattern_phone, text)
    if phone:
        info_phone.append(phone)
    else:
        info_phone.append("No phone found")

    tel = re.findall(pattern_tel, text)
    if tel:
        info_tel.append(tel)
    else:
        info_tel.append("No telephone found")

    information.append(info_email)
    information.append(info_phone)
    information.append(info_tel)
    return information
# ----------------- #


# --- [ Whois ] --- #
def whoiss(url):
    domain = domain_http(url)

    try:
        domain_info = whois.whois(domain)
        str(domain_info).replace('#','-')
        domain_name = f"domain name : {domain_info.domain_name}"
        registrar = f" registrar : {domain_info.registrar}"
        whois_server = f"whois server : {domain_info.whois_server}"
        referral_url = f"referral url : {domain_info.referral_url}"
        updated_date = f"updated date : {domain_info.updated_date}"
        creation_date = f"creation date : {domain_info.creation_date}"
        expiration_date = f"expiration date : {domain_info.expiration_date}"
        name_servers = f"name server : {domain_info.name_servers}"
        status = f"status : {domain_info.status}"
        emails = f"emails : {domain_info.emails}"
        dnssec = f"dnssec : {domain_info.dnssec}"
        name = f"name : {domain_info.name}"
        org = f"org : {domain_info.org}"
        address = f"address : {domain_info.address}"
        city = f"status : {domain_info.city}"
        state = f"status : {domain_info.state}"
        registrant_postal_code = f"registrant postal code : {domain_info.registrant_postal_code}"
        country = f"country : {domain_info.country}"
        all_info = []
        all_info.append(domain_name)
        all_info.append(registrar)
        all_info.append(whois_server)
        all_info.append(referral_url)
        all_info.append(updated_date)
        all_info.append(creation_date)
        all_info.append(expiration_date)
        all_info.append(name_servers)
        all_info.append(status)
        all_info.append(emails)
        all_info.append(dnssec)
        all_info.append(name)
        all_info.append(org)
        all_info.append(address)
        all_info.append(city)
        all_info.append(state)
        all_info.append(registrant_postal_code)
        all_info.append(country)
        return all_info
    except :
        print("Error")
# ----------------- #


# --- [ fix_name_of_screenshots ] --- #
def fix_name_screenshots(url):
    if url.startswith("https://") :
        url = url.replace("https://","")
        if url.startswith("www."):
            url = url.replace("www." , "")
    elif url.startswith("http://") :
        url = url.replace("http://","")
        if url.startswith("www."):
            url = url.replace("www." , "")
    
    for i in range (0 , len(url)):
        if url[i] == '.':
            url = url.replace('.' , '_')
        elif url[i] == '/':
            url = url.replace('/' , '_')    
    return str(url)
# ----------------- #

# --- [ screenshot ] --- #
def screenshot(url):
    browser = webdriver.Chrome()
    browser.get(url)
    browser.save_screenshot(fix_name_screenshots(url) + ".png")
    browser.quit()
# ----------------- #


# --- [ wappalyzer ] --- #
def wappalyzer(url):
    wappalyzers = Wappalyzer.latest()
    response = requests.get(url)
    web = WebPage.new_from_response(response)
    langs = wappalyzers.analyze(web)
    return langs 
# ----------------- #



def print_all(url,depth):
    if depth == 1:
        print(get_url(url,args.tag))
        print(wappalyzer(url))
        print(whoiss(url))
        print(regex(url))
        result = requests.get(f"https://api.u3er.xyz/Recon/recon-get.php?link={str(url)}&title={title(url)}&status={str(status_code(url))}&subdomain={str(sub_domain(url))}&port={str(port(url))}&wapplayzer={str(wappalyzer(url))}&whois={str(whoiss(url))}&regex={str(regex(url))}")
        if result.status_code == 200 :
            print("ok")
        with open("report.txt", "a") as file:
            file.write(str(url) + title(url) + "\n" + str(status_code(url)) + "\n" + str(sub_domain(url)) + "\n" + str(port(url)) + "\n" + str(wappalyzer(url)) + "\n" + str(whoiss(url)) + "\n" + str(regex(url)) + "\n\n\n")
        for i in range(0 , len(links)):

            print(status_code(links[i]))
            print(sub_domain(links[i]))
            print(port(links[i]))
            with open("report.txt", "a") as file:
                file.write(links[i] + "\n" + title(url) + "\n" + str(status_code(links[i] )) + "\n" + str(sub_domain(links[i])) + "\n" + str(port(links[i])) + str(wappalyzer(links[i])) + "\n" + str(whoiss(url)) + "\n" + str(regex(url)) + "\n\n\n")
                result = requests.get(f"https://api.u3er.xyz/Recon/recon-get.php?link={links[i]}&title={title(links[i])}&status={str(status_code(links[i] ))}&subdomain={str(sub_domain(links[i]))}&port={str(port(links[i]))}&wapplayzer={str(wappalyzer(links[i]))}&whois={str(whoiss(links[i]))}&regex={str(regex(url))}")
                if result.status_code == 200 :
                    print("ok")
            # screenshot(links[i])
    elif depth == 2:
        print(get_url(url , args.tag))
        print(wappalyzer(url))
        print(whoiss(url))
        print(regex(url))
        result = requests.get(f"https://api.u3er.xyz/Recon/recon-get.php?link={str(url)}&title={title(url)}&status={str(status_code(url))}&subdomain={str(sub_domain(url))}&port={str(port(url))}&wapplayzer={str(wappalyzer(url))}&whois={str(whoiss(url))}&regex={str(regex(url))}")
        if result.status_code == 200 :
            print("ok")
        with open("report.txt", "a") as file:
            file.write(str(url) + title(url) + "\n" + str(status_code(url)) + "\n" + str(sub_domain(url)) + "\n" + str(port(url)) + "\n" + str(wappalyzer(url)) + "\n" + str(whoiss(url)) + "\n" + str(regex(url)) + "\n\n\n")
        for i in range(0 , len(links_depth)):
            print(status_code(links_depth[i]))
            print(sub_domain(links_depth[i]))
            print(port(links_depth[i]))
            with open("report.txt", "a") as file:
                file.write(links_depth[i] + "\n" + title(links_depth[i]) + "\n" + str(status_code(links_depth[i] )) + "\n" + str(sub_domain(links_depth[i])) + "\n" + str(port(links_depth[i])) + str(wappalyzer(links_depth[i])) + "\n" + str(whoiss(url)) + "\n" + str(regex(url)) + "\n\n\n")
                result = requests.get(f"https://api.u3er.xyz/Recon/recon-get.php?link={links_depth[i]}&title={title(links_depth[i])}&status={str(status_code(links_depth[i] ))}&subdomain={str(sub_domain(links_depth[i]))}&port={str(port(links_depth[i]))}&wapplayzer={str(wappalyzer(links_depth[i]))}&whois={str(whoiss(links_depth[i]))}&regex={str(regex(url))}")
                if result.status_code == 200 :
                    print("ok")
            # screenshot(links_depth[i])


if args.url and args.tag and args.depth:
    print_all(args.url,args.depth)
else :
    banner()

