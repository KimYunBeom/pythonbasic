import pickle

# write binary
# profile_file = open('profile.pickle', 'wb')
# profile = {"이름":"박명수", "나이":30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # 변수 정보를 파일에 저장
# profile_file.close()

# read binary
profile_file = open('profile.pickle', 'rb')
profile = pickle.load(profile_file) # 파일의 정보를 변수에 불러오기
print(profile)
profile_file.close()
