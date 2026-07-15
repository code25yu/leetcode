class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(str(len(s))+'#'+s)
        return ''.join(encoded)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        n = len(s)

        while i < n:
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            start = j + 1
            end = start + length
            result.append(s[start:end])

            i = end

        return result
