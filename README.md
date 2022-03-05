# Your IP is mine
====
Hola! Esta herramienta sirve para sacar información de una IP


Requisitos
=====
* Python 3.x
* termcolor
* colorama


Instalacion
====
    pkg intall python3
    pkg intall git
    git clone https://github.com/LikLG-BalooSaurio/Your-IP-is-Mine
    cd Your-IP-is-Mine
    chmod +x *
    python3 -m pip install -r requirements.txt 
    python3 yIPim.py



Informacion
====
* ASN
* City
* Country
* Country Code
* ISP
* Latitude
* Longtitude
* Organization
* Region Code
* Region Name
* Timezone
* Zip Code


Uso
====
```
uso: yipim.py [-h] [-m] [-t TARGET] [-T file] [-u User-Agent]
                        [-U file] [-g] [--noprint] [-v] [--nolog] [-x PROXY]
                        [-X file] [-e file] [-ec file] [-ex file]


Argumentos opcionales:

  -h, --help            show this help message and exit
  -m, --my-ip           Get Geolocation info for my IP address.
  -t TARGET, --target TARGET
                        IP Address or Domain to be analyzed.
  -T file, --tlist file
                        A list of IPs/Domains targets, each target in new line.
  -u User-Agent, --user-agent User-Agent
                        Set the User-Agent request header (default: IP2GeoLocation 2.0.3).
  -U file, --ulist file
                        A list of User-Agent strings, each string in new line.
  -g                    Open IP location in Google maps with default browser.
  --noprint             IPGeolocation will print IP Geolocation info to terminal. It is possible to tell IPGeolocation n
ot to print results to terminal with this option.
  -v, --verbose         Enable verbose output.
  --nolog               IPGeolocation will save a .log file. It is possible to tell IPGeolocation not to save those log
files with this option.
  -x PROXY, --proxy PROXY
                        Setup proxy server (example: http://127.0.0.1:8080)
  -X file, --xlist file
                        A list of proxies, each proxy url in new line.
  -e file, --txt file   Export results.
  -ec file, --csv file  Export results in CSV format.
  -ex file, --xml file  Export results in XML format.
```

