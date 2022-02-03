# zip함수 - 길이가 같은 리스트들의 자료구조를 하나 묶어줄 수 잇다.
list1 = ["python", "respberry PI", "IOT", "MQTT"]
list2 = ["basic", "라즈베리파이의 사용방법", "IOT플랫폼구축", "통신"]
list3 = (88, 48, 48, 40)

for subject, info, time in zip(list1, list2, list3):
    print(" {} : {} ({})".format(subject, info, time))