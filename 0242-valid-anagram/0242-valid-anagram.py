# Solution4
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # # Solution 1
        # return sorted(s) == sorted(t)

        # # Solution2
        # if len(s) != len(t):
        #     return False
        # count = {}

        # # s의 문자 개수를 센다 (+1)
        # for char in s:
        #     count[char] = count.get(char, 0) + 1
        
        # # t의 문자 개수를 뺀다 (-1)
        # for char in t:
        #     count[char] = count.get(char, 0) - 1

        # # 모든 값이 0이면 개수가 정확히 일치한다는 뜻
        # for value in count.values():
        #     if value != 0:
        #         return False

        # return True

        # # Solution3
        # # 문제 조건에서 s, t가 소문자 영어 알파벳(a-z, 26개)로만 이루어져 있다고 했으므로, 딕셔너리 대신 크기 26짜리 배열을 써도 됨.
        # if len(s) != len(t):
        #     return False
        
        # count = [0] * 26  # a~z, 26개 알파벳 전용 카운터
        
        # # ord()는 문자를 아스키(ASCII) 코드 번호로 변환해주는 파이썬 내장 함수
        # # count의 각 원소 c를 하나씩 꺼내서 c == 0인지 (0과 같은지) True/False로 바꾼다 
        # for i in range(len(s)):
        #     count[ord(s[i]) - ord('a')] += 1
        #     count[ord(t[i]) - ord('a')] -= 1

        # return all(c == 0 for c in count)
        # # all()은 괄호 안의 모든 값이 True일 때만 True를 반환하는 내장 함수
        
        # Solution4
        return Counter(s) == Counter(t)
