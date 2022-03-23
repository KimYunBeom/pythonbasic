# 'w' : overwrite
# score_file = open('score.txt', 'w', encoding='utf-8')
# print('수학 : 0', file=score_file)
# print('영어 : 50', file=score_file)
# score_file.close()

# 'a' : append
# score_file = open('score.txt', 'a', encoding='utf-8')
# score_file.write('과학 : 80')
# score_file.write('\n')
# score_file.write('코딩 : 100')
# score_file.close()

# 'r' : read1
# score_file = open('score.txt', 'r', encoding='utf-8')
# print(score_file.read())
# score_file.close()

# 'r' : read2
# score_file = open('score.txt', 'r', encoding='utf-8')
# print(score_file.readline(), end='') # 줄별로 읽기, 읽은 후 다음 줄로 커서 이동
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# print(score_file.readline(), end='')
# score_file.close()

# 'r' : read3
# score_file = open('score.txt', 'r', encoding='utf-8')
# while True:
#   line = score_file.readline()
#   if not line:
#     break
#   print(line, end='')
# score_file.close()

# 'r' : read4
score_file = open('score.txt', 'r', encoding='utf-8')
lines = score_file.readlines() # list로 저장
for line in lines:
  print(line, end='')
score_file.close()
