def encode( strs: list[str]) -> str:
        stringlist=[]
        word=''
        for string in strs:
           Deciphor=str(len(string))+ '#'
           word = word +Deciphor+ string
        stringlist.append(word)
        return stringlist
text=["neet","code","love","you"]
ex=encode(strs=text)

print(ex)