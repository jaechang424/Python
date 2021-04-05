f = open("파일.txt", 'w', encoding='utf-8')
for i in range(1, 11):
    f.write(f"{i}번째 줄 ~\n")
f.close()

f = open("파일.txt", 'r', encoding="utf-8")
while True:
    line = f.readline()
    if not line: 
        print(line)
        break
    print(line)
f.close()