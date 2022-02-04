# 1. 문자열을 입력받아 거꾸로 출력될 수 있도록 작성하기
#   입력데이터 : python
#   출력데이터 : nohtyp
answer = input("입력데이터: ")
print("출력데이터: " + answer[::-1])
print("*" * 60)

# for i in range(len(answer)-1,-1,-1):
#     print(answer[i], end="")
# print("")

# for index, value in enumerate(answer):
#     print(answer[index], end="")

# outputstr = ""
# size = len(answer)
# for i in range(size):
#     outputstr = outputstr + answer[size-(i+1)]
# print(outputstr)
# 2. 입력받는 문자열 중 소문자 a가 있음면 대문자 A로 변경해서 출력하기
answers = input("입력데이터: ")
print("출력데이터:", end=" ")
for i in answers:
    if i == "a":
        print("A", end="")
    else:
        print(i, end="")
print("")
print("*" * 60)

# 3. 입력받은 문자열 대신 오른쪽으로 3칸 뒤에 있는 문자의 조합으로 출력하기

answeres = input("입력데이터: ")
casercipher = list(answeres)

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

# 1부터 10000까지의 숫자에서 8이라는 숫자가 총 몇번 나오는지 체크하기
# 8이 포함되어 있는 숫자의 숫자를 카운팅하는 것이 아니라 8이라는 숫자가 몇 번 나오는지 카운트