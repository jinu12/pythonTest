# 각각의 문자들을 알파벳 상의 세번째 오른쪽 문자로 치환하는 간단한 치환 암호기
# print(chr(ord(ch)+3))
casercipher = list("everyday we have is one more than we deserve")
for i in range(len(casercipher)):
    print(casercipher[i], end="")
print("")

for i in range(len(casercipher)):
    if casercipher[i] == "x":
        print("a", end="")
    elif casercipher[i] == "y":
        print("b", end="")
    elif casercipher[i] == "z":
        print("c", end="")
    elif casercipher[i] == " ":
        print(" ", end="")
    else:
        print(chr(ord(casercipher[i])+3), end="")
print("")

print("*" * 60)

answer = input("암호화 할 문자를 입력해주세요. : ")
casercipher= list(answer)

print("출력데이터: ", end="")
for i in range(len(casercipher)):
    if casercipher[i] == "x":
        print("a", end="")
    elif casercipher[i] == "y":
        print("b", end="")
    elif casercipher[i] == "z":
        print("c", end="")
    else:
        print("", chr(ord(casercipher[i])+3), end="")

