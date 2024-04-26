class Solution:
    def repeatedCharacter(self, s: str) -> str:
        countletters=[]
        for letters in s:
            if letters in countletters:
                return letters
            else:
                countletters.append(letters)
