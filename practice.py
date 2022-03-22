# print('Python', 'Java', sep=',')

# print('Python', 'Java', 'JavaScript', sep=' vs ')

# print('Python', 'Java', 'JavaScript', sep=',', end='?') # sep : 구분자 처리, end : 끝부분 처리
# print('무엇이 더 재미있을까요?')

# import sys
# print('Python', 'Java', file=sys.stdout)
# print('Python', 'Java', file=sys.stderr)

# # 시험 성적
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# # .items()로 파라미터1에 키, 파라미터2에 값을 추출
# for subject, score in scores.items(): 
#   # print(subject, score)
#   # ljust(8) : 8개 공간 확보 후, 왼쪽 정렬하여 글자를 출력
#   # rjust(4) : 4개 공간 확보 후, 오른쪽 정렬하여 글자를 출력
#   print(subject.ljust(8), str(score).rjust(4), sep=':') 

# # 은행 대기순번표
# # 001, 002, 003, ...
# # .zfill(3) : 3개 공간 확보 후, 남은 공간에 0을 채움
# for num in range(1, 21): 
#   print('대기번호 : ' + str(num).zfill(3))

# input()은 항상 str을 return
answer = input('아무 값이나 입력하세요 : ')
print('입력하신 값은 ' + str(answer) + '입니다.')
