from time import sleep
from os import system as sys




# "Enjoy"

#          ___     _,.--.,_
#       .-~   ~--"~-.   ._ "-.
#      /      ./_    Y    "-. \
#     Y       :~     !         Y
#     lq p    |     /         .|
#  _   \. .-, l    /          |j
# ()\___) |/   \_/";          !
#  \._____.-~\  .  ~\.      ./
#             Y_ Y_. "vr"~  T   
#             (  (    |L    j   - ayush0x1
#             [nn[nn..][nn..]   - https://github.com/ayush0x1
#         ~~~~~~~~~~~~~~~~~~~~~~~



class requre:
     req="apt install x11-repo"
     ins="apt install polybar geany python-tkinter neofetch openbox tigervnc alacritty feh jp2a cowsay xcompmgr firefox pcmanfm  zip git rofi -y"

### courser(pointer) 
def courser():
     sys('mkdir -p ~/.icons ~/.icons/default ~/tmp && curl -L https://archive.org/download/win-sur-white-cursors.tar/WinSur-white-cursors.tar.gz -o ~/tmp/winsur.tar.gz && tar -xzf ~/tmp/winsur.tar.gz -C ~/.icons && rm ~/tmp/winsur.tar.gz && printf "[Icon Theme]\nInherits=WinSur-white-cursors\n" > ~/.icons/default/index.theme && printf "export XCURSOR_THEME=WinSur-white-cursors\nexport XCURSOR_SIZE=24\n" > ~/.xprofile')



### openbox theme 
def theme():
     sys("wget https://archive.org/download/themes_202601/themes.zip -O /data/data/com.termux/files/usr/share/themes/th.zip && cd /data/data/com.termux/files/usr/share/themes && unzip th.zip")




### polybar 
def wall():
     from colorama import Fore, Back, Style, init
     init(autoreset=True)

     sys("clear")
     print(Style.BRIGHT + Fore.GREEN + "\n[+] Polybar configuring")
     sleep(3)
     sys("mkdir ~/.config/polybar")
     sys("cd ~/.config/polybar")
     sys("wget https://archive.org/download/polybar_20260319/polybar.zip && unzip polybar.zip && rm polybar.zip")
     sys("cd polybar-themes && bash setup.sh && rm -rf polybar-themes")
     sys("mkdir ~/Picture && mkdir ~/Desktop && mkdir ~/Videos && mkdir ~/Project && mkdir Downloads && mkdir Public && cd ~/")
     

### bashrc 

def bashrc():
    sys("cd ~/")
    brc = '#!/bin/bash\nclear\nneofetch --ascii_distro Radix'
    with open("../.bashrc", "w") as file:
        file.write(brc)

      
      



### ayush0x1 software(app)    
def app():
     sys("wget https://archive.org/download/app_20260319/app.zip -O /data/data/com.termux/files/usr/share/app.zip && cd  /data/data/com.termux/files/usr/share/ && unzip app.zip")
     print("\n")
     sys("mkdir -p /data/data/com.termux/files/usr/lib/firefox/distribution")
     sys("touch /data/data/com.termux/files/usr/lib/firefox/distribution/policies.json")
     print("[+] Done.")
     policies = open('/data/data/com.termux/files/usr/lib/firefox/distribution/policies.json', 'w') 
     policies.write('{\n  "policies": {\n    "Homepage": {\n      "URL": "https://litecraft-search.netlify.app/",\n      "Locked": true\n    },\n    "Preferences": {\n      "browser.startup.homepage": {"Value": "https://your-website.com", "Status": "locked"}\n    }\n  }\n}')
     policies.close()






### vnc support 
def vnc():

      from colorama import Fore, Back, Style, init
      import os
      init(autoreset=True)

      sys("clear")
      print(Fore.BLUE + "[+] Tigervnc ")
      sleep(3)

      vnc_dir = "/data/data/com.termux/files/home/.vnc"
      os.makedirs(vnc_dir, exist_ok=True)
      sys("pkill Xvnc && vncserver && cd ~/.vnc/")

      con = """\nexport DISPLAY=:1\nsed -i  "s|<name>.*</name>|<name>Prismatic-Night</name>|g" ~/.config/openbox/rc.xml\nxcompmgr &\nfeh --randomize --bg-fill /data/data/com.termux/files/usr/share/app/wall/* &\ncd /data/data/com.termux/files/usr/share/app/ && python app.py &\n(sleep 2 && ~/.config/polybar/docky/launch.sh &>/dev/null &) &\nexec openbox-session &\nsleep 2\nopenbox --reconfigure &"""
      with open(f"{vnc_dir}/xstartup", "w") as file:
          file.write(con)

      print("[+] Done")

      text = "pkill Xvnc\nrm -rf $HOME/.vnc/localhost:1.pid\nrm -rf $PREFIX/tmp/.X1-lock\nrm -rf $PREFIX/tmp/.X11-unix/X1\nvncserver :1 -geometry 1280x720\necho '[+] Started  '\n"
      with open("start-desktop", "w") as file:
          file.write(text)

      sys("pkill Xvnc")
      sys(
      "chmod +x start-desktop && "
      "chmod +x ~/.vnc/xstartup && "
      "clear && "
      "mv start-desktop $PREFIX/bin && "
      "start-desktop"
      )

      sys("clear && cowsay -f koala  'If you enjoy this project, please support it. A lot of time and effort went into creating it.'")
      sys("start-desktop")
      print("\n")
      print(Style.BRIGHT + Fore.BLUE + "[+] Next time use command : start-desktop")
      print(Style.BRIGHT + Fore.BLUE + "[+] More features coming soon")


### install 
def main():
     from colorama import Fore, Back, Style, init

     sys("jp2a https://assets.stickpng.com/images/613098fd48f1e30004910189.png  --color ")
     print(Style.BRIGHT + Fore.BLUE + "[+] Created by: ayush \n")
     sleep(4)
     sys(requre.req)
     sys(requre.ins)
     print(Style.BRIGHT + Fore.BLUE + "\n[+] Instaled")
     sleep(3)

try:
   main()
   wall()
   
   app()
   courser()
   bashrc()
   
   theme()
   vnc()
        
except ImportError:
   print("[!] Installing : pip install rich colorama==0.4.6 \n")
   sys("pip install rich colorama==0.4.6")
   sys("python install.py")
   print("\n")

