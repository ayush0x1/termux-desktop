from time import sleep
from os import system as sys


class requre:
     req="apt install x11-repo"
     ins="apt install polybar openbox tigervnc alacritty feh jp2a xcompmgr firefox pcmanfm  zip git rofi -y"


def courser():
     sys('mkdir -p ~/.icons ~/.icons/default ~/tmp && curl -L https://archive.org/download/win-sur-white-cursors.tar/WinSur-white-cursors.tar.gz -o ~/tmp/winsur.tar.gz && tar -xzf ~/tmp/winsur.tar.gz -C ~/.icons && rm ~/tmp/winsur.tar.gz && printf "[Icon Theme]\nInherits=WinSur-white-cursors\n" > ~/.icons/default/index.theme && printf "export XCURSOR_THEME=WinSur-white-cursors\nexport XCURSOR_SIZE=24\n" > ~/.xprofile')


def theme():
     sys("wget https://archive.org/download/themes_202601/themes.zip -O /data/data/com.termux/files/usr/share/themes/th.zip && cd /data/data/com.termux/files/usr/share/themes && unzip th.zip")

def wall():
     from colorama import Fore, Back, Style, init
     init(autoreset=True)

     sys("clear")
     print(Style.BRIGHT + Fore.GREEN + "\n[+] Polybar configuring")
     sleep(3)
     sys("mkdir ~/.config/polybar")
     sys("cd ~/.config/polybar")
     sys("wget https://archive.org/download/polybar/polybar.zip && unzip polybar.zip && rm polybar.zip")
     sys("cd polybar-themes && bash setup.sh && rm -rf polybar-themes")
     sys("mkdir ~/Picture && mkdir Downloads && mkdir Public && cd ~/")
     print("wallpaper")
     sys("rm Picture/*")
     sys("wget https://ia600602.us.archive.org/15/items/wallpaper_202601/spy-x-family-anya-forger-hot-cocoa-lamppost-desktop-wallpaper-preview.jpg -O ~/Picture/wall.jpg ")



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

      con = """\nexport DISPLAY=:1\nsed -i  "s|<name>.*</name>|<name>Prismatic-Night</name>|g" ~/.config/openbox/rc.xml\nxcompmgr &\nfeh --bg-fill ~/Picture/wall.jpg &\n(sleep 2 && ~/.config/polybar/docky/launch.sh &>/dev/null &) &\nexec openbox-session &\nsleep 2\nopenbox --reconfigure &"""
      with open(f"{vnc_dir}/xstartup", "w") as file:
          file.write(con)

      print("[+] Done")

      text = "pkill Xvnc\nvncserver :1 -geometry 1280x720"
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
      sys("clear && start-desktop")
      print(Style.BRIGHT + Fore.GREEN + "[+] Next time use command : start-desktop")




def main():
     from colorama import Fore, Back, Style, init

     sys("jp2a https://assets.stickpng.com/images/613098fd48f1e30004910189.png  --color ")
     print(Style.BRIGHT + Fore.BLUE + "Created by: ayush \n")
     sleep(2)
     sys(requre.req)
     sys(requre.ins)
     print("\n[+] Instaled")
     sleep(2)

try:
   main()
   wall()
   courser()
   theme()
   vnc()
        
except ImportError:
   print("[!] Installing : pip install colorama==0.4.6 \n")
   sys("pip install colorama==0.4.6")
   sys("python install.py")

