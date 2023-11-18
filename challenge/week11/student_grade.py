class Student:
    def __init__(self, name, kor, math, eng): # 생성자 작성
        self.name = name # 이름 초기화
        self.kor = kor # 국어 초기화
        self.math = math # 수학 초기화
        self.eng = eng # 영어 초기화

# 파일을 읽어서 각 줄을 리스트로 저장
lines = open("student.csv", "r", encoding="utf8").readlines()

# TODO 1: 학생 정보를 딕셔너리에 저장
student_data = {}

header = lines[0].strip().split(',') # 쉼표(,) 기준으로 단어 쪼개기
for line in lines[1:]: # '실바' 부분부터 시작
    tokens = line.strip().split(',') # 쉼표(,) 기준으로 쪼갠 학생 이름을 tokens에 저장
    student_name = tokens[0] # tokens에 저장된 학생 이름들을 student_name에 저장
    scores = [float(score) if '.' in score else int(score) for score in tokens[1:]] # 학생 별 점수를 scores에 저장
    student_data[student_name] = dict(zip(header[1:], scores)) # 각 학생 별로 저장한 점수를 student_data 딕셔너리에 저장

# TODO 2: 학생 별 평균 점수를 계산
average_scores = {}

# TODO 3: Student 클래스 활용하여 학생 정보 저장
students = []

for student_name, scores in student_data.items(): # student_data의 key 값과 value 값을 각각 학생 이름과 점수로 저장
    average_score = sum(scores.values()) / len(scores) if len(scores) > 0 else 0 # 학생의 점수 평균값을 average_score에 저장
    average_scores[student_name] = average_score # 저장된 평균을 각 학생 별로 저장

    # Student 클래스를 사용하여 학생 객체 생성 및 리스트에 추가
    student = Student(name=student_name, kor=scores['국어'], math=scores['수학'], eng=scores['영어'])
    students.append(student) # students에 추가

# 결과 출력
print("-----학생들의 평균 점수-----")
for student_name, average_score in average_scores.items():
    print(f'{student_name}의 평균 점수는   {average_score} 입니다.') # 학생들의 평균 점수 출력

# 평균 점수를 파일로 출력 (average.txt)
file = open("average.txt", 'w', encoding='utf8') # average.txt 파일 생성
for student_name, average_score in average_scores.items():
    file.write(f'{student_name}의 평균 점수는   {average_score} 입니다.\n')# 출력된 학생드르이 평균 점수를 average.txt에 입력
file.close() # 파일 종료