import win32com.client
import pythoncom
import os
En = 'en_US'
Ja = 'ja_JP'
Es = 'es_ES'
Cn = 'zh_CN'
Kr = 'ko_KR'
lang = int(input('1) English    2) Spanish  3) Japanese  4) Korean   5)Chinese \n Select the number of the language : ' ))

if lang == 5 :
    lang_new = Cn
elif lang == 4:
    lang_new = Kr
elif lang == 3 :
    lang_new = Ja
elif lang == 2 :
    lang_new = Es
elif lang == 1 :
    lang_new = En



desktop = r'C:\Users\Public\Desktop' 
path = os.path.join(desktop, f'league {lang_new}.lnk')
target = r'C:\Riot Games\League of Legends\LeagueClient.exe'
icon = r'C:\Riot Games\League of Legends\LeagueClient.exe'




shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.Arguments = '--locale='+f'{lang_new}'
shortcut.IconLocation = icon
shortcut.WindowStyle = 7
shortcut.save()

#TXT
file = open("print.txt", "w")
target = str(target)
file.write(target)
file.close()