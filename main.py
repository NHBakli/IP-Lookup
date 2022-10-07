from pystyle import Anime, Colorate, Colors, Center, System, Write
import requests
import os

System.Size(140, 40)
System.Title("IP Lookup")
System.Clear()

ascii = """
 ######  ######            ###       #####    #####   ### ###  ### ###  ######   
   ##    ### ###           ###      ### ###  ### ###  ### ###  ### ###  ### ###  
   ##    ### ###           ###      ### ###  ### ###  ### ##   ### ###  ### ###  
   ##    ######            ###      ### ###  ### ###  #####    ### ###  ######   
   ##    ###               ###      ### ###  ### ###  ### ##   ### ###  ###      
   ##    ###               ###  ##  ### ###  ### ###  ### ###  ### ###  ###      
 ######  ###               #######   #####    #####   ### ###   #####   ###      
                                                                                  
"""[1:]

flower = '''
                   .,,. 
            .,v%;mmmmmmmm;%%vv,. 
         ,vvv%;mmmvv;vvvmmm;%vvvv,    .,,. 
  ,, ,vvvnnv%;mmmvv;%%;vvmmm;%vvvv%;mmmmmmm, 
,mmmmmm;%%vv%;mmmvv;%%;vvmmm;%v%;mmmmmmmmmmm 
mmmmmmmmmmm;%%;mmmvv%;vvmmm;%mmmmmmmmmmmmmm' 
`mmmmmmmmmmmmmm%;mmv;vmmm;mmmmmmm;%vvvvvv' 
    `%%%%%;mmmmmmmm;v%v;mmmmmm;%vvvnnvv' 
     vvvvvv%%%%; IP Lookup mmm;%vvvnnnn 
     `vvnnnnvvv%%%;m;mmmmm;%vvnnmmnnvv' 
      vvnmmnnnnvvv%%mmmm;%vvnnmmmnnnvv 
      `vvnmmmnnvvv%mmm;%vvnnmmmmnnnvv' 
       `vvnmmmmvv%mmm;%vvnnmmmmnnnvv' 
        `vvnmmmvv%mm;%vvvnnmmmnnvvv' 
          `vvnmmvv%m;%vvvvnmnvvvv' 
           .;;vvvvvm;%vvvvvvvv' 
        .;;;;;;;;;;;;;;;;;;;;, 
       ;;;;;;';;;;;;;;;;;'`;;;;;, 
      .;;;'    `;;;;;;;;'   `;;;;;. 
     .;;'        `;;;;;'      `;;;; 
     ;'           :`;;'         ;;' 
     ;            : ;'    ,    ,'             . 
      `           :'.:   .;;,.        .,;;;;;;' 
                  ::::   ;;,;;;,     ;;;,;;;;' 
                  ;;;;   `;;;,;;    .,';;;;' 
                  ;;;;      `';; ,;;' 
                ,;;;;;         .;',. 
                  `;;;;       .;'  ';,. 
                   `;;;.     .;'   ,;;,;;,. 
                    ;;;;    .;'    `;;;;,;;; 
                    ;;;;   .;'       `;;,;;' 
                    `;;;,;;'           `;' 
                     ;;;; 
                     ;;;;. 
                     `;;;;;,. 
                      ;;;;' 
                      ;;;; 
                      ;;;;
'''[1:]


Anime.Fade(Center.Center(flower), Colors.yellow_to_red, Colorate.Vertical, interval=0.025, enter=True)

System.Clear()
print("\n" * 2)
print(Colorate.Diagonal(Colors.yellow_to_red, Center.XCenter(ascii)))
print("\n" * 5)
ip = Write.Input("Veuillez entrer une adresse IP -> ", Colors.yellow_to_red, interval=0.005)


response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,mobile,proxy,hosting,query')

data = response.json()

ipaddress = data['query']
continett = data['continent']
countryy = data['country']
zipcode = data['zip']
latt = data['lat']
lonn = data['lon']
ispp = data['isp']
orgg = data['org']
proxyy = data['proxy']
hostingg = data['hosting']

Write.Print(f'IP: {ipaddress}\nContinent: {continett}\nPays: {countryy}\nCode Postal: {zipcode}\nLat: {latt}\nLon: {lonn}\nFournisseur: {ispp}\nOrg: {orgg}\nProxy: {proxyy}\nHosting: {hostingg}', Colors.yellow_to_red, interval=0.005)

search = Write.Input("\n\n\n\nAppuyer sur entrer pour fermer la fenêtre...\n\nTaper 1 si vous voulez relancer le tools -> ", Colors.yellow_to_red, interval=0.005)
if search == "1":
    os.system("python main.py")












