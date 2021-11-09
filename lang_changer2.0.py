import win32com.client
import pythoncom
import os



while True :
    lista = ['','en_US','es_ES','ja_JP','ko_KR','zh_CN','zh_TW','es_MX','fr_FR','de_DE','it_IT','pl_PL','ro_RO','pt_BR','hu_HU','ru_RU','tr_TR']
    lang = input("1) English\n2) Spanish\n3) Japanese\n4) Korean\n5) Chinese isn't working\n6) Taiwan\n7) Latino Spanish\n8) French\n9) Deutsch\n10) Italian\n11) Polish\n12) Romanian\n13) Greek\n14) Portuguese\n15) Hungary\n16) Russian\n17) Turkish\n\nSelect the number of the language : ")
    
    try :
        lang = int(lang)
    except :
        print('Choose a valid character (numbers)')
        
    lang_new = lista[lang]


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