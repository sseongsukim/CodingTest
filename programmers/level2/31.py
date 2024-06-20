"""
전화번호 목록

"""
def solution(phone_book):
    phone_book = sorted(phone_book, key= lambda x: len(x))
    for first_number, next_number in zip(phone_book[:-1], phone_book[1:]):
        if next_number.startswith(first_number):
            return False
    return True


# print(solution(["119", "97674223", "1195524421"])) # False
# print(solution(["123","456","789"])) # True
print(solution(["12","123","1235","567","88"])) # False

