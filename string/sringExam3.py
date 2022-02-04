# 주어진 문자열에서 알파벳의 각 갯수를 딕셔너리에 넣어서 출력하세요
# [조건]
# - 문자열인 경우만 체크하기
# - 빈 딕셔너리를 만들어서 값 저장하기
# - 대소문자 구분없이 작업하기
# - 영문자가 key로 , 반복횟수가 value
# - fpransdmf

# [출력형태]
# {'p':16,

mystr = """
            Python is an easy to learn, powerful programming language. 
            It has efficient high-level data structures and a simple but effective 
            approach to object-oriented programming.
            Python’s elegant syntax and dynamic typing, together with its interpreted nature, 
            make it an ideal language for scripting and rapid application development in many areas on most platforms.
        """

dic1 = {1: "a", 2: "b"}
# print(1 not in dic1)

alphabetdict = dict()
count = 0
for c in mystr:
    if c.isalpha():
        # print(c, end=" ")
        c = c.lower()
        if c in alphabetdict:
            alphabetdict[c] = alphabetdict[c] + 1
        else:
            alphabetdict[c] = 1
        count = count + 1
    else:
        pass

sorted_alphane = sorted(alphabetdict.items())
print(sorted_alphane)

print("*" * 300)

# count = 0
#
# mystrlist = []
# # mystrlist = list(mystr)
#
# for c in mystr:
#     if c.isalpha():
#         mystrlist.append(c)
#     else:
#         pass
#
# mydict = {}
#
# print(len(mystrlist))
# for i in range(len(mystrlist)):
#     for j in range(i):
#         if mystrlist[i].isupper():
#             mystrlist[i] = mystrlist[i].lower()
#         if mystrlist[i] == mystrlist[j]:
#             mydict.update({mystrlist[i]: (count + 1)})
#             if mydict[mystrlist[i]] == mystrlist[i]:
#                 mydict[mystrlist[i]] = mydict[mystrlist[i]] + 1
#             else:
#                 mydict[mystrlist[i]] = 1
#
# sorted_mydict = sorted(mydict.items())
# print(sorted_mydict)
 