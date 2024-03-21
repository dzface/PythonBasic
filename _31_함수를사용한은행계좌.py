

# 계좌개설

def open_account(name): # 매개변수O 반환값O 인 함수
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name

def deposit(input):
    global balance
    balance += input
    print(f"{input}원이 입금 되었습니다. 잔액은 {balance+input}원 입니다.")
    return balance + input
def withdraw(input):
    global balance
    if balance >= input:
        print(f"{input}원이 출금 되었습니다. 잔액은 {balance-input}원 입니다.")
        return balance -input
    else:
        print(f"출금에 실패했습니다.")

balance = 0 # 현재 잔액을 외부에서 선언 함 *** 중요 개념 immutable 한 balance 변수는 함수 내부로 불러올때는 global을 추가해야 함***
name = open_account("곰돌이 사육사")
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
print(f"{name}의 잔액은 {balance} 입니다.")


def global_check ():
    print()
    ls=balance # ls는 mutable 자료형으로 함수 외내부가 동일
    ls2 = 3000 # 함수내 ls2와 변수 ls2는 다른 것

ls = []
ls2 = 0
