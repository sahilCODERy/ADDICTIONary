import json
import random
import difflib
from difflib import get_close_matches
import webbrowser

index=json.load(open("dictionary_compact.json"))
print("\n------------------------ DICTIONARY by CODERY ------------------------\n")

def get(word):
    res=index[word]
    for i,val in enumerate(res):
        print("{}: {}".format(i+1, val))
    print("\nGive me a word again")    
    
print("Give me a word, I'll find you its Meaning; To get random meaning say 'Im Bored'")
print("To Stop say 'Enough Codery'")    
while(1):
    word=input()
    word=word.lower()
    
    bored=["im bored","i'm bored"]
    randw=random.choice(list(index.keys()))
    if(word not in bored ):    
        if(word in index):
            print("")
            get(word)
        elif(word=="enough codery"):
            break;    
        elif(word not in index):
            indexr=list(index.keys())
            close=get_close_matches(word,indexr,n=3,cutoff=0.7)
            if(len(close)>0):
                print("Did you mean {},{},{}?".format(close[0],close[1],close[2]))
                ch=input("enter 1, 2, 3 or No for None:\n").lower()
                if(ch=='1'):
                    print(close[0],"\n")
                    get(close[0])
                elif(ch=='2'):
                    print(close[1],"\n")
                    get(close[1])
                elif(ch=='3'):
                    print(close[2],"\n")
                    get(close[2])    
                elif(ch=='no'):
                    print("Sorry, Not Sure what you're lookin for,  Let me search it on Google ")
                    webbrowser.open("https://www.google.com/search?q={}".format(word))
                else:
                    print("Invalid Query, Try Again ")                    
            else:
                print("Can't Find Such a Word, Let me search it on Google ")
                webbrowser.open("https://www.google.com/search?q={}".format(word))
        
    else:
        print("word:",randw,":")
        get(randw)
