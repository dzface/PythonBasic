
import numpy as np
# 배열이란? 순서가 있는 같은 종류의 데이터가 저장된 집합을 의미

data1 = [1,2,3,4,5,6,7] # 리스트 생성
a1 = np.array(data1) #리스트를 넘파이 배열로 변환
print(data1) # [1,2,3,4,5,6,7]
print(a1) # [1 2 3 4 5 6 7]

data2 = [0,1,3,5, 0.4, 3.14, 9.99] # 리스트는 데이터형이 달라도 입력가능
a2 = np.array(data2) # 넘파이 배열은 같은 타입이어야 하므로 자동 형변환 정수, 실수 포함되어 있으면 모두 실수로 변환
print(a2)
x = np.array([0.1 , 0.2, 0.3])
print(x)
print(x.shape) # 배열의 형태를 나타냄
print(x.dtype) # 배열 요소의 데이터 타입을 반환
y = np.array(([1,2,3], [4,5,6]))
print(y)
print(y.shape)
print(y.dtype)

# 범위를 지정해 배열 생성 : arange()
a3 = np.arange(0, 10, 2) # 0~10 미만 2씩 증가

# 배열의 형태 변경
a4 = np.arange(12).reshape(4, 3) # 0 ~ 12 미만의 배열을 생성 배열의 구조를 4 * 3 구조로 변경
print(a4)

# 범위의 시작과 끝, 그리고 범위를 지정하는 메서드 : linspace()
a5 = np.linspace(1,10,20)
print(a5)

# 0 ~ 파이값까지 동일한 간격으로 20개 데이터 생성
a6 = np.linspace(0, np.pi, 20)
print(a6)

# 특별한 형태의 배열 생성
a7 = np.zeros(10)
print(a7)

a8 = np.zeros((3,4)) # 0으로 초기화된 2차원 (3X4)배열 생성
print(a8)

a9 = np.ones(10)
print(a9)
a10 =np.ones((3,4))
print(a10)

# 단위 행렬 만들기 : n X n 인 정사각형의 행렬의 주대각선이 모두 1이고 나머지는 0인 행렬
a11 = np.eye(3)
print(a11)

# 배열의 데이터 타입 변환
a12 = np.array(['1.5', '0.62', '2', '3.14', '3.141592'])
print(a12)
print(a12.dtype)

num_a12 = a12.astype(float) # 문자열을 실수타입으로 변환
print(num_a12)

a13 = np.array(['1','3','5','7','9'])
num_a13 = a13.astype(int) # 문자열을 정수타입으로 변환
print(num_a13)

# 난수 배열 생성하기
a14 = np.random.rand(2,3) # 0 ~ 1 미만의 임의의 실수값 생성 2X3
print(a14)
a15 = np.random.rand(2,3,4) # 난수를 생성하는 3차원 배열 생성
print(a15)

# 지정한 범위에 해당하는 정수로 난수 배열 생성
a16 = np.random.randint(10, size=(3,4))
print(a16)

# 배열의 연산 : 배열은 사칙연산을 할 수 있음. 단 배열의 형태가 같아야 함
arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])
print( arr1 + arr2)
print (arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)

# 요소별 비교 연산
arr3 = np.array([10, 20, 30, 40, 50])
print (arr3 > 20)

# 통계를 위한 연산 : 배열의 합, 표준편자, 분산, 최대값과 최소값, 누적최솟값, 누적합과 누적곱
# 통계에서 많이 사용하는 메서드를 제공
arr4 = np.arange(5) # 0 ~ 5 미만의 값 생성
print(f"합계 : {arr4.sum()}")
print(f"평균 : {arr4.mean}")
print(f"표준 편차 : {arr4.std()}")
print(f"분산 : {arr4.var()}")
print(f"최소값 : {arr4.min()}")
print(f"최대값 : {arr4.max()}")

# 배열의 인덱싱 / 슬라이싱
arr5 = np.array([1,2,3,4,5])
# 인덱싱
print(arr5[3])
print(arr5[:4]) # 0부터 4미만까지 값을 잘라냄

# Universal 함수 : 배열의 원소별 연산을 지원 하는 함수
arr6 = np.array([1,2,3,4,5])
arr7 = np.arange(6,11)
print(arr6)
print(arr7)
print("add : ", np.add(arr6, arr7))
print("sub : ", np.subtract(arr6, arr7))
print("mul : ", np.multiply(arr6, arr7))
print("div : ", np.divide(arr6, arr7))
print("pow : ", np.power(arr6, arr7))

# 행렬 연산 : 행렬간의 연산, 다차원 배열 대해서~
matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6],[7,8]])
# 행렬 덧셈
print(np.add(matrix1, matrix2))
print(np.subtract(matrix2, matrix1))
print(np.multiply(matrix1, matrix2))

# 전치행렬 : 행과 열을 교환
matrix3 = np.array([[1,2],[3,4]])
inverse_matrix3 = np.transpose(matrix3)
print (inverse_matrix3)

# 정렬과 탐색
x_sort = np.array([9,8,7,12,13,2,1,5,2])
print(np.amin(x_sort))
print(np.amax(x_sort))
print(np.argmin(x_sort)) # 최소값이 있는 위치
print(np.argmax(x_sort)) # 최대값이 있는 위치
print(np.sort(x_sort)) # 오름차순 정렬
print(np.argsort(x_sort)) # 값의 인덱스

# 브로드캐스팅 : 배열의 크기가 다른 경우에 대한 연산 지원
aa = np.array([1,2,3])
bb = np.array([[4],[5],[6]])
cc = aa + bb
print(cc)