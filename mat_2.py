def revword(word:str) -> str:
    result=word[::-1]
    result=result.lower()
    return(result)

def countword()->int:
    file=open("text.txt")
    counter=0
    index=0
    for i in file:
        if index==0:
            word=i.lower()
            index=1
            word=word.rstrip()
        line=i.split()
        for j in line:
            reWord=revword(j)
            if(reWord==word):
                counter=counter+1
    return counter 


           

