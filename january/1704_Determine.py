class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {
            'a': False,
            'e': False,
            'i': False,
            'o': False,
            'u': False,
            'A': False,
            'E': False,
            'I': False,
            'O': False,
            'U': False
        }
        half_vowels = 0
        half_length = len(s) // 2
        for i in range(half_length):
            if s[i] in vowels:
                half_vowels += 1
            if s[-i-1] in vowels:
                half_vowels -= 1
        return half_vowels == 0