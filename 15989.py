Test_case = int(input())
Answer = []
for _ in range(Test_case): Answer.append(int(input()))

Num = max(Answer)+1
Sheet = [[0,0,0] for _ in range(Num)]


def AnswerSheet():
        Sheet[1], Sheet[2], Sheet[3] = [1,0,0], [1,1,0], [1,1,1]

        for i in range(4, Num):
                Sheet[i][0] = Sheet[i-1][0]
                Sheet[i][1] = Sheet[i-2][0] + Sheet[i-2][1]
                Sheet[i][2] = Sheet[i-3][0] + Sheet[i-3][1] + Sheet[i-3][2]
AnswerSheet()
for _ in range(Test_case): print(Sheet[Answer[_]][0]+Sheet[Answer[_]][1]+Sheet[Answer[_]][2])
