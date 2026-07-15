# from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # # Solution1
        # return sorted(s) == sorted(t)

        # # Solution2
        # return Counter(s) == Counter(t)

        # Solution3
        if len(s) != len(t):
            return False
        count = {}
        for ch in s:
            count[ch] = count.get(ch, 0) + 1
        # dict.get(key, default)
        # key: 찾고 싶은 키
        # default: 그 키가 딕셔너리에 없을 경우 대신 반환할 값 (생략하면 None)
        # count.get(ch, 0) → 현재까지 센 개수를 가져옴 (없으면 0)
        # 여기에 + 1을 해서 → "지금 문자 하나를 새로 발견했으니 개수를 1 늘린다"
        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] == 0:
                del count[ch]    
        return len(count) == 0
