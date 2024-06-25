"""
[3차] 파일명 정렬

"""
def solution(files):
    answer = []
    for file in files:
        head = ""
        number = ""
        index = 0
        while not file[index].isdigit():
            head += file[index]
            index += 1
        while file[index].isdigit():
            number += file[index]
            index += 1
            if index >= len(file):
                break
        tail = file[index:]
        answer.append((head, number, tail))
    answer.sort(key= lambda x: (x[0].lower(), int(x[1])))
    return [a + b + c for a, b, c in answer]






print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
# ["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"]
# print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
# ["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"]