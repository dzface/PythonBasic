
# 딕셔너리를 이용한 커피 메뉴 만들기

menu_dic = {
    "Americano": ["Coffee", 2000, "기본 커피 입니다."],
    "Esspresso": ["Coffee", 2500, "진한 커피 입니다."],
    "Latte": ["Coffee", 4000, "우유가 들어 있는 커피 입니다."],
    "ColdBrew": ["Coffee", 4500, "연유가 들어 있는 커피 입니다."],
    "GreenTea": ["Tea", 4500, "녹차 입니다."],
    "BlackTea": ["Tea", 4500, "홍차 입니다."],
    "MlilTea" : ["Tea", 4000, "우유가 포함된 차 입니다."],
    "PeachAde": ["Ade", 5000, "복숭아 에이드 입니다."],
    "GreenAde": ["Ade", 5000, "포도 에이드 입니다."],
    "LemonAde": ["Ade", 4500, "레몬 에이드 입니다."]
}
while True:
    print("메뉴를 선택 하세요.")
    menu = input("[1] 메뉴 보기, [2] 메뉴 조회, [3] 추가 하기, [4] 삭제 하기, [5] 종료 하기 : ")
    if menu ==1:
        for key in menu_dic: # key의 갯수만큼 순회
            print(key,":",menu_dic[key]) # 키와 키에 해당하는 값을 출력

    elif menu ==2:
        serch_menu = input("조회할 메뉴 입력 :")
        if serch_menu in menu_dic:
            print(menu_dic[serch_menu])
        elif menu == 3:
            add_name = input("찾는 메뉴가 없습니다.")

    elif menu ==3:
        add_menu = input("추가 할 메뉴 입력 : ")
        if add_menu not in menu_dic:
            cate = input("카테고리 입력 : ")
            price= int(input("가격 입력 : "))
            desc = input("메뉴 설명 : ")
            menu_dic[add_menu] = [cate,price,desc]
        else: print("메뉴가 이미 존재 합니다.")
    elif menu == 4:
        del_menu = input("삭제 할 메뉴 입력 : ")
        if del_menu in menu_dic:
            del_menu[del_menu]
        else: print("삭제 할 메뉴가 없습니다.")
        for key in menu_dic:
            print(key, ":", menu_dic[key])
    elif menu == 5:
        print("영업을 종료 합니다.")
        break
    else:
        print("해당 메뉴가 없습니다. 다시조회 하세요.")
        continue
