## lzmcore.py - useful module of Lazymux
# -*- coding: utf-8 -*-
import os
import sys
import time

lazymux_banner = """
.-.                                           
: :                                           
: :    .--.  .---. .-..-.,-.,-.,-..-..-..-.,-.
: :__ ' .; ; `-'_.': :; :: ,. ,. :: :; :`.  .'
:___.'`.__,_;`.___;`._. ;:_;:_;:_;`.__.':_,._;
                    .-. :                     
                    `._.'                     
"""
backtomenu_banner = """
  [99] Back to main menu
  [00] Exit the Lazymux
"""
allmodule = 0
def install_pacakage(installer, packs):
	if installer == 'apt' and allmodule == 0:
		os.system('apt update && apt upgrade')
	for v in packs:
		os.system(installer+' install ' + v)

def wget_(links):
	for v in links:
		os.system('wget ' + v)

def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
	curdir = os.getcwd()

def backtomenu_option():
	if(allmodule == 0):
		print ('###### Done')
		print (backtomenu_banner)
		backtomenu = input("lzmx > ")
		
		if backtomenu == "99":
			restart_program()
		elif backtomenu == "00":
			sys.exit()
		else:
			print ("\nERROR: Wrong Input")
			time.sleep(2)
			restart_program()
	else:
		os.system('apt update && apt upgrade')
		print ('###### Processing...\n')

def banner():
	print (lazymux_banner)

def nmap():
	print ('\n###### Installing Nmap')
	install_pacakage('apt', ['nmap'])
	print ("###### Type 'nmap' to start.")
	backtomenu_option()

def red_hawk():
	print ('\n###### Installing RED HAWK')
	install_pacakage('apt', ['git', 'php'])
	os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
	os.system('mv RED_HAWK ~')
	backtomenu_option()

def dtect():
	print ('\n###### Installing D-Tect')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/shawarkhanethicalhacker/D-TECT-1')
	os.system('mv D-TECT-1 ~')
	backtomenu_option()

def sqlmap():
	print ('\n###### Installing sqlmap')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/sqlmapproject/sqlmap')
	os.system('mv sqlmap ~')
	backtomenu_option()

def infoga():
	print ('\n###### Installing Infoga')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['requests', 'urllib3', 'urlparse'])
	os.system('git clone https://github.com/m4ll0k/Infoga')
	os.system('mv Infoga ~')
	backtomenu_option()

def reconDog():
	print ('\n###### Installing ReconDog')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/UltimateHackers/ReconDog')
	os.system('mv ReconDog ~')
	backtomenu_option()

def androZenmap():
	print ('\n###### Installing AndroZenmap')
	install_pacakage('apt', ['nmap', 'curl'])
	os.system('curl -O http://override.waper.co/files/androzenmap.txt')
	os.system('mkdir ~/AndroZenmap')
	os.system('mv androzenmap.txt ~/AndroZenmap/androzenmap.sh')
	backtomenu_option()

def sqlmate():
	print ('\n###### Installing sqlmate')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['mechanize', 'bs4', 'HTMLparser', 'argparse', 'requests', 'urlparse2'])
	os.system('git clone https://github.com/UltimateHackers/sqlmate')
	os.system('mv sqlmate ~')
	backtomenu_option()

def astraNmap():
	print ('\n###### Installing AstraNmap')
	install_pacakage('apt', ['nmap', 'git'])
	os.system('git clone https://github.com/Gameye98/AstraNmap')
	os.system('mv AstraNmap ~')
	backtomenu_option()

def wtf():
	print ('\n###### Installing WTF')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['bs4', 'requests','HTMLParser','urlparse','mechanize','argparse'])
	os.system('git clone https://github.com/Xi4u7/wtf')
	os.system('mv wtf ~')
	backtomenu_option()

def easyMap():
	print ('\n###### Installing Easymap')
	install_pacakage('apt', ['php', 'git'])
	os.system('git clone https://github.com/Cvar1984/Easymap')
	os.system('mv Easymap ~')
	os.system('cd ~/Easymap && sh install.sh')
	backtomenu_option()

def xd3v():
	print ('\n###### Installing XD3v')
	install_pacakage('apt', ['curl'])
	os.system('curl -k -O https://gist.github.com/Gameye98/92035588bd0228df6fb7fa77a5f26bc2/raw/f8e73cd3d9f2a72bd536087bb6ba7bc8baef7d1d/xd3v.sh')
	os.system('mv xd3v.sh ~/../usr/bin/xd3v && chmod +x ~/../usr/bin/xd3v')
	print ('###### Done')
	print ("###### Type 'xd3v' to start.")
	backtomenu_option()

def crips():
	print ('\n###### Installing Crips')
	install_pacakage('apt', ['python2', 'git', 'openssl', 'curl', 'libcurl', 'wget'])
	os.system("git clone https://github.com/Manisso/Crips")
	os.system("mv Crips ~")
	backtomenu_option()

def sir():
	print ('\n###### Installing SIR')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['bs4', 'urllib2'])
	os.system("git clone https://github.com/AeonDave/sir.git")
	os.system("mv sir ~")
	backtomenu_option()

def xshell():
	print ('\n###### Installing Xshell')
	install_pacakage('apt', ['python2', 'lynx', 'figlet', 'ruby', 'php', 'nano', 'w3m'])
	os.system("git clone https://github.com/Ubaii/Xshell")
	os.system("mv Xshell ~")
	backtomenu_option()

def evilURL():
	print ('\n###### Installing EvilURL')
	install_pacakage('apt', ['python2', 'git', 'python3'])
	os.system("git clone https://github.com/UndeadSec/EvilURL")
	os.system("mv EvilURL ~")
	backtomenu_option()

def striker():
	print ('\n###### Installing Striker')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/UltimateHackers/Striker')
	os.system('mv Striker ~')
	os.system('cd ~/Striker && pip2 install -r requirements.txt')
	backtomenu_option()

def dsss():
	print ('\n###### Installing DSSS')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/stamparm/DSSS')
	os.system('mv DSSS ~')
	backtomenu_option()

def sqliv():
	print ('\n###### Installing SQLiv')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/Hadesy2k/sqliv')
	os.system('mv sqliv ~')
	backtomenu_option()

def sqlscan():
	print ('\n###### Installing sqlscan')
	install_pacakage('apt', ['php', 'git'])
	os.system('git clone http://www.github.com/Cvar1984/sqlscan')
	os.system('mv sqlscan ~')
	backtomenu_option()

def wordpreSScan():
	print ('\n###### Installing Wordpresscan')
	install_pacakage('apt', ['python2', 'python2-dev', 'clang', 'libxml2-dev', 'libxml2-utils', 'libxslt-dev'])
	os.system('git clone https://github.com/swisskyrepo/Wordpresscan')
	os.system('mv Wordpresscan ~')
	os.system('cd ~/Wordpresscan && pip2 install -r requirements.txt')
	backtomenu_option()

def wpscan():
	print ('\n###### Installing WPScan')
	install_pacakage('apt', ['ruby', 'curl'])
	os.system('git clone https://github.com/wpscanteam/wpscan')
	os.system('mv wpscan ~ && cd ~/wpscan')
	os.system('gem install bundle && bundle config build.nokogiri --use-system-libraries && bundle install && ruby wpscan.rb --update')
	backtomenu_option()

def wordpresscan():
	print ('\n###### Installing wordpresscan(2)')
	install_pacakage('apt', ['nmap', 'figlet', 'git'])
	os.system('git clone https://github.com/silverhat007/termux-wordpresscan')
	os.system('cd termux-wordpresscan && chmod +x * && sh install.sh')
	os.system('mv termux-wordpresscan ~')
	print ('###### Done')
	print ("###### Type 'wordpresscan' to start.")
	backtomenu_option()

def routersploit():
	print ('\n###### Installing Routersploit')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['requests'])
	os.system('git clone https://github.com/reverse-shell/routersploit')
	os.system('mv routersploit ~;cd ~/routersploit;pip2 install -r requirements.txt;termux-fix-shebang rsf.py')
	backtomenu_option()

def torshammer():
	print ('\n###### Installing Torshammer')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/dotfighter/torshammer')
	os.system('mv torshammer ~')
	backtomenu_option()

def slowloris():
	print ('\n###### Installing Slowloris')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/gkbrk/slowloris')
	os.system('mv slowloris ~')
	backtomenu_option()

def fl00d12():
	print ('\n###### Installing Fl00d & Fl00d2')
	install_pacakage('apt', ['python2', 'wget'])
	os.system('mkdir ~/fl00d')
	os.system('wget http://override.waper.co/files/fl00d.apk')
	os.system('wget http://override.waper.co/files/fl00d2.apk')
	os.system('mv fl00d.apk ~/fl00d/fl00d.py;mv fl00d2.apk ~/fl00d/fl00d2.py')
	backtomenu_option()

def goldeneye():
	print ('\n###### Installing GoldenEye')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/jseidl/GoldenEye')
	os.system('mv GoldenEye ~')
	backtomenu_option()

def xerxes():
	print ('\n###### Installing Xerxes')
	install_pacakage('apt', ['clang', 'git'])
	os.system('git clone https://github.com/zanyarjamal/xerxes')
	os.system('mv xerxes ~')
	os.system('cd ~/xerxes && clang xerxes.c -o xerxes')
	backtomenu_option()

def planetwork_ddos():
	print ('\n###### Installing Planetwork-DDOS')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/Hydra7/Planetwork-DDOS')
	os.system('mv Planetwork-DDOS ~')
	backtomenu_option()

def hydra():
	print ('\n###### Installing Hydra')
	install_pacakage('apt', ['hydra'])
	backtomenu_option()

def black_hydra():
	print ('\n###### Installing Black Hydra')
	install_pacakage('apt', ['python2', 'git', 'hydra'])
	os.system('git clone https://github.com/Gameye98/Black-Hydra')
	os.system('mv Black-Hydra ~')
	backtomenu_option()

def cupp():
	print ('\n###### Installing Cupp')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/Mebus/cupp')
	os.system('mv cupp ~')
	backtomenu_option()

def leethash():
	print ('\n###### Installing 1337Hash')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/Gameye98/1337Hash')
	os.system('mv 1337Hash ~')
	backtomenu_option()

def hash_buster():
	print ('\n###### Installing Hash-Buster')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/UltimateHackers/Hash-Buster')
	os.system('mv Hash-Buster ~')
	backtomenu_option()

def instaHack():
	print ('\n###### Installing InstaHack')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['requests'])
	os.system('git clone https://github.com/avramit/instahack')
	os.system('mv instahack ~')
	backtomenu_option()

def indonesian_wordlist():
	print ('\n###### Installing indonesian-wordlist')
	install_pacakage('apt', ['git'])
	os.system('git clone https://github.com/geovedi/indonesian-wordlist')
	os.system('mv indonesian-wordlist ~')
	backtomenu_option()

def facebook_bruteForce():
	print ('\n###### Installing Facebook Brute Force')
	install_pacakage('apt', ['python2', 'wget'])
	install_pacakage('pip2', ['mechanize'])
	os.system('mkdir ~/facebook-brute')
	os.system('wget http://override.waper.co/files/facebook.apk')
	os.system('wget http://override.waper.co/files/password.apk')
	os.system('mv facebook.apk ~/facebook-brute/facebook.py;mv password.apk ~/facebook-brute/password.txt')
	backtomenu_option()

def facebook_BruteForce():
	print ('\n###### Installing Facebook Brute Force 2')
	install_pacakage('apt', ['python2', 'wget'])
	install_pacakage('pip2', ['mechanize'])
	os.system('wget http://override.waper.co/files/facebook2.apk')
	os.system('wget http://override.waper.co/files/password.apk')
	os.system('mkdir ~/facebook-brute-2')
	os.system('mv facebook2.apk ~/facebook-brute-2/facebook2.py && mv password.apk ~/facebook-brute-2/password.txt')
	backtomenu_option()

def fbBrute():
	print ('\n###### Installing Facebook Brute Force 3')
	install_pacakage('apt', ['python2', 'wget'])
	install_pacakage('pip2', ['mechanize'])
	os.system('wget http://override.waper.co/files/facebook3.apk')
	os.system('wget http://override.waper.co/files/password.apk')
	os.system('mkdir ~/facebook-brute-3')
	os.system('mv facebook3.apk ~/facebook-brute-3/facebook3.py && mv password.apk ~/facebook-brute-3/password.txt')
	backtomenu_option()

def webdav():
	print ('\n###### Installing Webdav')
	install_pacakage('apt', ['python2', 'openssl', 'curl', 'libcurl'])
	install_pacakage('pip2', ['urllib3', 'chardet', 'certifi', 'idna', 'requests'])
	os.system('mkdir ~/webdav')
	os.system('curl -k -O http://override.waper.co/files/webdav.txt;mv webdav.txt ~/webdav/webdav.py')
	backtomenu_option()

def xGans():
	print ('\n###### Installing xGans')
	install_pacakage('apt', ['python2', 'curl'])
	os.system('mkdir ~/xGans')
	os.system('curl -O http://override.waper.co/files/xgans.txt')
	os.system('mv xgans.txt ~/xGans/xgans.py')
	backtomenu_option()

def webmassploit():
	print ('\n###### Installing Webdav Mass Exploiter')
	install_pacakage('apt', ['python2', 'openssl', 'curl', 'libcurl'])
	install_pacakage('pip2', ['requests'])
	os.system("curl -k -O https://pastebin.com/raw/K1VYVHxX && mv K1VYVHxX webdav.py")
	os.system("mkdir ~/webdav-mass-exploit && mv webdav.py ~/webdav-mass-exploit")
	backtomenu_option()

def wpsploit():
	print ('\n###### Installing WPSploit')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone git clone https://github.com/m4ll0k/wpsploit')
	os.system('mv wpsploit ~')
	backtomenu_option()

def sqldump():
	print ('\n###### Installing sqldump')
	install_pacakage('apt', ['python2', 'curl'])
	install_pacakage('pip2', ['google'])
	os.system('curl -k -O https://gist.githubusercontent.com/Gameye98/76076c9a282a6f32749894d5368024a6/raw/6f9e754f2f81ab2b8efda30603dc8306c65bd651/sqldump.py')
	os.system('mkdir ~/sqldump && chmod +x sqldump.py && mv sqldump.py ~/sqldump')
	backtomenu_option()

def websploit():
	print ('\n###### Installing Websploit')
	install_pacakage('apt', ['git', 'python2'])
	install_pacakage('pip2', ['scapy'])
	os.system('git clone https://github.com/The404Hacking/websploit')
	os.system('mv websploit ~')
	backtomenu_option()

def sqlokmed():
	print ('\n###### Installing sqlokmed')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['urllib2'])
	os.system('git clone https://github.com/Anb3rSecID/sqlokmed')
	os.system('mv sqlokmed ~')
	backtomenu_option()

def zones():
	print ('###### zones')
	install_pacakage('apt', ['php', 'git'])
	os.system("git clone https://github.com/Cvar1984/zones")
	os.system("mv zones ~")
	backtomenu_option()

def metasploit():
	print ('\n###### Installing Metasploit')
	install_pacakage('apt', ['wget', 'git', 'curl'])
	os.system("wget https://gist.githubusercontent.com/Gameye98/d31055c2d71f2fa5b1fe8c7e691b998c/raw/09e43daceac3027a1458ba43521d9c6c9795d2cb/msfinstall.sh")
	os.system("mv msfinstall.sh ~;cd ~;sh msfinstall.sh")
	print ("###### Type 'msfconsole' to start.")
	backtomenu_option()

def commix():
	print ('\n###### Installing Commix')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/commixproject/commix')
	os.system('mv commix ~')
	backtomenu_option()

def brutal():
	print ('\n###### Installing Brutal')
	install_pacakage('apt', ['git'])
	os.system('git clone https://github.com/Screetsec/Brutal')
	os.system('mv Brutal ~')
	backtomenu_option()

def a_rat():
	print ('\n###### Installing A-Rat')
	install_pacakage('apt', ['git', 'python2'])
	os.system('git clone https://github.com/Xi4u7/A-Rat')
	os.system('mv A-Rat ~')
	backtomenu_option()

def knockmail():
	print ('\n###### Installing KnockMail')
	install_pacakage('apt', ['git', 'python2'])
	install_pacakage('pip2', ['validate_email', 'pyDNS'])
	os.system('git clone https://github.com/4w4k3/KnockMail')
	os.system('mv KnockMail ~')
	backtomenu_option()

def spammer_grab():
	print ('\n###### Installing Spammer-Grab')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['requests'])
	os.system('git clone https://github.com/p4kl0nc4t/spammer-grab')
	os.system('mv spammer-grab ~')
	backtomenu_option()

def hac():
	print ('\n###### Installing Hac')
	install_pacakage('apt', ['php', 'git'])
	os.system('git clone https://github.com/Cvar1984/Hac')
	os.system('mv Hac ~')
	backtomenu_option()

def spammer_email():
	print ('\n###### Installing Spammer-Email')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['argparse', 'requests'])
	os.system("git clone https://github.com/p4kl0nc4t/Spammer-Email")
	os.system("mv Spammer-Email ~")
	backtomenu_option()

def rang3r():
	print ('\n###### Installing Rang3r')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['optparse', 'termcolor'])
	os.system("git clone https://github.com/floriankunushevci/rang3r")
	os.system("mv rang3r ~")
	backtomenu_option()

def sh33ll():
	print ('\n###### Installing SH33LL')
	install_pacakage('apt', ['python2', 'git'])
	os.system("git clone https://github.com/LOoLzeC/SH33LL")
	os.system("mv SH33LL ~")
	backtomenu_option()

def social():
	print ('\n###### Installing Social-Engineering')
	install_pacakage('apt', ['python2', 'perl'])
	os.system("git clone https://github.com/LOoLzeC/social-engineering")
	os.system("mv social-engineering ~")
	backtomenu_option()

def spiderbot():
	print ('\n###### Installing SpiderBot')
	install_pacakage('apt', ['git', 'php'])
	os.system("git clone https://github.com/Cvar1984/SpiderBot")
	os.system("mv SpiderBot ~")
	backtomenu_option()

def ngrok():
	print ('\n###### Installing Ngrok')
	install_pacakage('apt', ['git'])
	os.system('git clone https://github.com/themastersunil/ngrok')
	os.system('mv ngrok ~')
	backtomenu_option()

def sudo():
	print ('\n###### Installing sudo')
	install_pacakage('apt', ['git', 'ncurses-utils'])
	os.system('git clone https://github.com/st42/termux-sudo')
	os.system('mv termux-sudo ~ && cd ~/termux-sudo && chmod 777 *')
	os.system('cat sudo > /data/data/com.termux/files/usr/bin/sudo')
	os.system('chmod 700 /data/data/com.termux/files/usr/bin/sudo')
	backtomenu_option()

def ubuntu():
	print ('\n###### Installing Ubuntu')
	install_pacakage('apt', ['git', 'python2'])
	os.system('git clone https://github.com/Neo-Oli/termux-ubuntu')
	os.system('mv termux-ubuntu ~ && cd ~/termux-ubuntu && bash ubuntu.sh')
	backtomenu_option()

def fedora():
	print ('\n###### Installing Fedora')
	install_pacakage('apt', ['git', 'wget'])
	os.system('wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh')
	os.system('mv termux-fedora.sh ~')
	backtomenu_option()

def nethunter():
	print ('\n###### Installing Kali NetHunter')
	install_pacakage('apt', ['git'])
	os.system('git clone https://github.com/Hax4us/Nethunter-In-Termux')
	os.system('mv Nethunter-In-Termux ~')
	backtomenu_option()

def blackbox():
	print ('\n###### Installing BlackBox')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['python2', 'optparse', 'passlib'])
	os.system('git clone https://github.com/jothatron/blackbox')
	os.system('mv blackbox ~')
	backtomenu_option()

def xattacker():
	print ('\n###### Installing XAttacker')
	install_pacakage('apt', ['git', 'perl'])
	install_pacakage('cpnm', ['HTTP::Request', 'LWP::Useragent'])
	os.system('git clone https://github.com/Moham3dRiahi/XAttacker')
	os.system('mv XAttacker ~')
	backtomenu_option()

def vcrt():
	print ('\n###### Installing VCRT')
	install_pacakage('apt', ['git', 'python2'])
	os.system('git clone https://github.com/LOoLzeC/Evil-create-framework')
	os.system('mv Evil-create-framework ~')
	backtomenu_option()

def socfish():
	print ('\n###### Installing SocialFish')
	install_pacakage('apt', ['git', 'python2'])
	install_pacakage('pip2', ['wget'])
	os.system('git clone https://github.com/UndeadSec/SocialFish')
	os.system('mv SocialFish ~')
	backtomenu_option()

def ecode():
	print ('\n###### Installing ECode')
	install_pacakage('apt', ['php', 'git'])
	os.system('git clone https://github.com/Cvar1984/Ecode')
	os.system('mv Ecode ~')
	backtomenu_option()

def hashzer():
	print ('\n###### Installing Hashzer')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['requests'])
	os.system('git clone https://github.com/Anb3rSecID/Hashzer')
	os.system('mv Hashzer ~')
	backtomenu_option()

def xsstrike():
	print ('\n###### Installing XSStrike')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['fuzzywuzzy', 'prettytable', 'mechanize', 'HTMLParser'])
	os.system('git clone https://github.com/UltimateHackers/XSStrike')
	os.system('mv XSStrike ~')
	backtomenu_option()

def breacher():
	print ('\n###### Installing Breacher')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['requests', 'argparse'])
	os.system('git clone https://github.com/UltimateHackers/Breacher')
	os.system('mv Breacher ~')
	backtomenu_option()

def stylemux():
	print ('\n###### Installing Termux-Styling')
	install_pacakage('apt', ['git'])
	os.system('git clone https://github.com/BagazMukti/Termux-Styling-Shell-Script')
	os.system('mv Termux-Styling-Shell-Script ~')
	backtomenu_option()

def txtool():
	print ('\n###### Installing TXTool')
	install_pacakage('apt', ['git', 'python2', 'nmap', 'php', 'curl'])
	install_pacakage('pip2', ['requests'])
	os.system('git clone https://github.com/kuburan/txtool')
	os.system('mv txtool ~')
	backtomenu_option()

def passgencvar():
	print ('\n###### Installing PassGen')
	install_pacakage('apt', ['git', 'php'])
	os.system('git clone https://github.com/Cvar1984/PassGen')
	os.system('mv PassGen ~')
	backtomenu_option()

def owscan():
	print ('\n###### Installing OWScan')
	install_pacakage('apt', ['git', 'php'])
	os.system('git clone https://github.com/Gameye98/OWScan')
	os.system('mv OWScan ~')
	backtomenu_option()

def sanlen():
	print ('\n###### Installing santet-online')
	install_pacakage('apt', ['git', 'python2'])
	install_pacakage('pip2', ['requests'])
	os.system('git clone https://github.com/Gameye98/santet-online')
	os.system('mv santet-online ~')
	backtomenu_option()

def spazsms():
	print ('\n###### Installing SpazSMS')
	os.system('apt update && apt upgrade')
	os.system('apt install git python2 && pip2 install requests')
	os.system('git clone https://github.com/Gameye98/SpazSMS')
	os.system('mv SpazSMS ~')
	backtomenu_option()

def hasher():
	print ('\n###### Installing Hasher')
	install_pacakage('apt', ['git', 'python2'])
	install_pacakage('pip2', ['passlib', 'binascii', 'progressbar'])
	os.system('git clone https://github.com/ciku370/hasher')
	os.system('mv hasher ~')
	backtomenu_option()

def hashgenerator():
	print ('\n###### Installing Hash-Generator')
	install_pacakage('apt', ['git', 'python2'])
	install_pacakage('pip2', ['passlib', 'progressbar'])
	os.system('git clone https://github.com/ciku370/hash-generator')
	os.system('mv hash-generator ~')
	backtomenu_option()

def kodork():
	print ('\n###### Installing ko-dork')
	install_pacakage('apt', ['git', 'python2'])
	install_pacakage('pip2', ['urllib2'])
	os.system('git clone https://github.com/ciku370/ko-dork')
	os.system('mv ko-dork ~')
	backtomenu_option()

def snitch():
	print ('\n###### Installing snitch')
	install_pacakage('apt', ['git', 'python2'])
	os.system('git clone https://github.com/Smaash/snitch')
	os.system('mv snitch ~')
	backtomenu_option()

def osif():
	print ('\n###### Installing OSIF')
	install_pacakage('apt', ['git', 'python2'])
	install_pacakage('pip2', ['requests'])
	os.system('git clone https://github.com/ciku370/OSIF')
	os.system('mv OSIF ~')
	backtomenu_option()

def nk26():
	print ('\n###### Installing nk26')
	install_pacakage('apt', ['git', 'php'])
	os.system('git clone https://github.com/milio48/nk26')
	os.system('mv nk26 ~')
	backtomenu_option()

def devploit():
	print ('\n###### Installing Devploit')
	install_pacakage('apt', ['git', 'python2'])
	install_pacakage('pip2', ['urllib2'])
	os.system('git clone https://github.com/joker25000/Devploit')
	os.system('mv Devploit ~')
	backtomenu_option()

def hasherdotid():
	print ('\n###### Installing Hasherdotid')
	install_pacakage('apt', ['git', 'python2'])
	os.system('git clone https://github.com/galauerscrew/hasherdotid')
	os.system('mv hasherdotid ~')
	backtomenu_option()

def SocialBox():
	print ('\n###### Installing SocialBox')
	install_pacakage('apt', ['git'])
	os.system('git clone https://github.com/TunisianEagles/SocialBox.git')
	os.system('mv SocialBox ~')
	os.system('cd ~/SocialBox && chmod +x SocialBox.sh && chmod +x install-sb.sh && sh install-sb.sh && sh SocialBox.sh')
	backtomenu_option()

def namechk():
	print ('\n###### Installing Namechk')
	install_pacakage('apt', ['git'])
	os.system('git clone https://github.com/HA71/Namechk')
	os.system('mv Namechk ~')
	backtomenu_option()

def xlPy():
	print ('\n###### Installing xl-py')
	install_pacakage('apt', ['git', 'python'])
	os.system('git clone https://github.com/albertoanggi/xl-py')
	os.system('mv xl-py ~')
	backtomenu_option()

def beanshell():
	print ('\n###### Installing Beanshell')
	install_pacakage('apt', ['dpkg', 'wget'])
	os.system('wget https://github.com/amsitlab/amsitlab.github.io/raw/master/dists/termux/amsitlab/binary-all/beanshell_2.04_all.deb')
	os.system('dpkg -i beanshell_2.04_all.deb')
	os.system('rm beanshell_2.04_all.deb')
	print ("###### Type 'bsh' to start.")
	backtomenu_option()

def msfpg():
	print ('\n###### Installing MSF-Pg')
	install_pacakage('apt', ['git'])
	os.system('git clone https://github.com/haxzsadik/MSF-Pg')
	os.system('mv MSF-Pg ~')
	print ("###### Done")
	backtomenu_option()

def touchurl():
	print ('\n###### Installing TouchURL')
	install_pacakage('apt', ['git', 'python'])
	install_pacakage('pip', ['colorama', 'parse'])
	os.system('git clone https://github.com/SkyKnight-Team/TouchUrl')
	os.system('mv TouchUrl ~')
	print ("###### Done")
	backtomenu_option()

def webconn():
	print ('\n###### Installing WebConn')
	install_pacakage('apt', ['git', 'python'])
	os.system('git clone https://github.com/SkyKnight-Team/WebConn')
	os.system('mv WebConn ~')
	print ("###### Done")
	backtomenu_option()

def binploit():
	print ('\n###### Installing Binary Exploitation')
	install_pacakage('apt', ['gdb', 'radare2', 'ired', 'ddrescue', 'bin-utils', 'yasm', 'strace', 'ltrace', 'cdb', 'hexcurse', 'memcached', 'llvmdb'])
	print ("###### Tutorial: https://youtu.be/3NTXFUxcKPc")
	backtomenu_option()

def textr():
	print ('\n###### Installing Textr')
	install_pacakage('apt', ['dpkg', 'wget'])
	os.system('wget https://raw.githubusercontent.com/amsitlab/textr/master/textr_1.0_all.deb')
	os.system('dpkg -i textr_1.0_all.deb')
	os.system('rm textr_1.0_all.deb')
	print ("###### Type 'textr' to start.")
	backtomenu_option()

def apsca():
	print ('\n###### Installing ApSca')
	install_pacakage('apt', ['dpkg', 'wget'])
	os.system('wget https://raw.githubusercontent.com/BlackHoleSecurity/apsca/master/apsca_0.1_all.deb')
	os.system('dpkg -i apsca_0.1_all.deb')
	os.system('rm apsca_0.1_all.deb')
	print ("###### Type 'apsca' to start.")
	backtomenu_option()

def amox():
	print ('\n###### Installing amox')
	install_pacakage('apt', ['dpkg', 'wget'])
	os.system('wget https://gitlab.com/dtlily/amox/raw/master/amox_1.0_all.deb')
	os.system('dpkg -i amox_1.0_all.deb')
	os.system('rm amox_1.0_all.deb')
	print ("###### Type 'amox' to start.")
	backtomenu_option()

def fade():
	print ('\n###### Installing FaDe')
	install_pacakage('apt', ['python2', 'git'])
	install_pacakage('pip2', ['requests'])
	os.system('git clone https://github.com/Gameye98/FaDe')
	os.system('mv FaDe ~')
	backtomenu_option()

def ginf():
	print ('\n###### Installing GINF')
	install_pacakage('apt', ['git', 'php'])
	os.system('git clone https://github.com/Gameye98/GINF')
	os.system('mv GINF ~')
	backtomenu_option()

def auxile():
	print ('\n###### Installing AUXILE')
	install_pacakage('apt', ['git', 'python2'])
	install_pacakage('pip2', ['requests', 'bs4', 'pexpect'])
	os.system('git clone https://github.com/CiKu370/AUXILE')
	os.system('mv AUXILE ~')
	backtomenu_option()

def inther():
	print ('\n###### Installing inther')
	install_pacakage('apt', ['git', 'ruby'])
	os.system('git clone https://github.com/Gameye98/inther')
	os.system('mv inther ~')
	backtomenu_option()

def hpb():
	print ('\n###### Installing HPB')
	install_pacakage('apt', ['dpkg', 'wget'])
	os.system('wget https://raw.githubusercontent.com/Cvar1984/HPB/master/html_0.1_all.deb')
	os.system('dpkg -i html_0.1_all.deb')
	os.system('rm html_0.1_all.deb')
	print ("###### Type 'hpb' to start.")
	backtomenu_option()

def DDosy():
	print ('\n###### Installing DDOSy')
	install_pacakage('apt', ['python2', 'git'])
	os.system('git clone https://github.com/Sanix-Darker/DDosy')
	os.system('mv DDosy ~')
	backtomenu_option()

def getAllModule(category):
	global allmodule
	allmodule = 1
	if category == "Information_Gathering":
		print ("### Installing all Information_Gathering Modules on LazyMux\n")
		os.system('rm -rf Information_Gathering && mkdir Information_Gathering')
		os.system('mv Information_Gathering ~')
		os.system('cd ~/Information_Gathering')
		nmap()
		red_hawk()
		dtect()
		sqlmap()
		infoga()
		reconDog()
		androZenmap()
		sqlmate()
		astraNmap()
		wtf()
		easyMap()
		blackbox()
		xd3v()
		crips()
		sir()
		evilURL()
		striker()
		xshell()
		owscan()
		osif()
		devploit()
		namechk()
		auxile()
		inther()
		ginf()
	elif category == "Vulnerability_Scanner":
		print ("###  Installing all Vulnerability_Scanner Modules on LazyMux \n")
		os.system('rm -rf Vulnerability_Scanner && mkdir Vulnerability_Scanner')
		os.system('mv Vulnerability_Scanner ~')
		os.system('cd ~/Vulnerability_Scanner')
		nmap()
		androZenmap()
		astraNmap()
		easyMap()
		red_hawk()
		dtect()
		dsss()
		sqliv()
		sqlmap()
		sqlscan()
		wordpreSScan()
		wpscan()
		sqlmate()
		wordpresscan()
		wtf()
		rang3r()
		striker()
		routersploit()
		xshell()
		sh33ll()
		blackbox()
		xattacker()
		owscan()
	elif category == "Stress_Testing":
		print ("### Installing all Stress_Testing Modules on LazyMux ...\n")
		os.system('rm -rf Stress_Testing && mkdir Stress_Testing ')
		os.system('mv Stress_Testing ~')
		os.system('cd ~/Stress_Testing')
		torshammer()
		slowloris()
		fl00d12()
		goldeneye()
		xerxes()
		planetwork_ddos()
		hydra()
		black_hydra()
		xshell()
		sanlen()
		DDosy()
	elif category == "Password_Attacks":
		print ("   Installing all Password_Attacks Modules on LazyMux \n")
		os.system('rm -rf Password_Attacks && mkdir Password_Attacks')
		os.system('mv Password_Attacks ~')
		os.system('cd ~/Password_Attacks')
		hydra()
		facebook_bruteForce()
		facebook_BruteForce()
		fbBrute()
		black_hydra()
		hash_buster()
		leethash()
		cupp()
		instaHack()
		indonesian_wordlist()
		xshell()
		social()
		blackbox()
		hashzer()
		hasher()
		hashgenerator()
		nk26()
		hasherdotid()
		SocialBox()
	elif category == "Web_Hacking":
		print ("### Installing all Web_Hacking Modules on LazyMux \n")
		os.system('rm -rf Web_Hacking && mkdir Web_Hacking ')
		os.system('mv Web_Hacking ~')
		os.system('cd ~/Web_Hacking')
		sqlmap()
		webdav()
		xGans()
		webmassploit()
		wpsploit()
		sqldump()
		websploit()
		sqlmate()
		sqlokmed()
		zones()
		xshell()
		sh33ll()
		xattacker()
		xsstrike()
		breacher()
		owscan()
		kodork()
		apsca()
		amox()
		fade()
		auxile()
		hpb()
		inther()
	elif category == "Exploitation_Tools":
		print ("### Installing all Exploitation_Tools Modules on LazyMux \n")
		os.system('rm -rf Exploitation_Tools && mkdir Exploitation_Tools')
		os.system('mv Exploitation_Tools ~')
		os.system('cd ~/Exploitation_Tools')
		metasploit()
		commix() 
		sqlmap() 
		brutal() 
		a_rat() 
		wpsploit() 
		websploit() 
		routersploit() 
		blackbox() 
		xattacker() 
		txtool() 
		msfpg() 
		binploit()
	elif category == "Sniffing_and_Spoofing":
		print ("### Installing all Sniffing_and_Spoofing Modules on LazyMux \n")
		os.system('rm -rf Sniffing_and_Spoofing && mkdir Sniffing_and_Spoofing')
		os.system('mv Sniffing_and_Spoofing ~')
		os.system('cd ~/Sniffing_and_Spoofing')
		knockmail()
		spammer_grab()
		hac()
		spammer_email()
		socfish()
		sanlen()
		spazsms()
	elif category == "Other":
		print ("### Installing all Other Modules on LazyMux\n")
		os.system('rm -rf Other && mkdir Other')
		os.system('mv Other ~')
		os.system('cd ~/Other')
		spiderbot()
		ngrok()
		sudo()
		ubuntu()
		fedora()
		nethunter()
		vcrt()
		ecode()
		stylemux()
		passgencvar()
		xlPy()
		beanshell()
		webconn()
		touchurl()
		textr()
	else:
		print (" Nothing selected.")
	os.system('cd ../')
	allmodule = 0
	backtomenu_option()