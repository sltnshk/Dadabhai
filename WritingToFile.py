s = open("Readme.md","r")
#if f.mode == "r":
content = s.read()
UI =(input("Enter the name of file"))
print(UI)
f = open("UI.txt","W+")
s.write("",content)

s.close()