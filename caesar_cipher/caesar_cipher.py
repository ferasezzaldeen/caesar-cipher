import nltk
from nltk.sem.logic import TRUTH_TYPE

nltk.download('words', quiet=True)
nltk.download('names', quiet=True)


from nltk.corpus import words,names

words_lest=words.words()
name_list=names.words()

def encrypt(string,key):
    encrypted_text=''
    string=string.lower()
    for x in string:
        temp=ord(x)
        if temp<97 or temp>122:
            encrypted_text+=x
        else:
            
            sol=(temp+key)
            if sol>122:
                shefted_letter=sol
                while shefted_letter>122:
                    shefted_letter=(shefted_letter%122)+96
            else:
                shefted_letter=sol%122
            new_letter=chr(shefted_letter)
            encrypted_text+=new_letter
       
    return encrypted_text


def decrypt(string,key):
    decrypted_text=''
    string=string.lower()
    for x in string:
        temp=ord(x)
        if temp<97 or temp>122:
            decrypted_text+=x
        else:
            
            sol=(temp-key)
            if sol<97:
                shefted_letter=sol
                while shefted_letter<97:
                    shefted_letter=(shefted_letter+26)
            else:
                shefted_letter=sol%122
            new_letter=chr(shefted_letter)
            decrypted_text+=new_letter

        
    return decrypted_text

def crack(string):
    accuracy={}
    temp=1
    for i in range(26):
        word_count=0
        iteretion=decrypt(string,temp)
        words_l=iteretion.split()
        for word in words_l:
            if word in words_lest or word in name_list or word.lower() in words_lest or word.upper() in words_lest:
                word_count+=1
        percentage = int(word_count / len(words_l) * 100)
        accuracy[temp]=percentage
        temp+=1
    real_key=max(accuracy, key=accuracy.get)
    return decrypt(string,real_key)



if __name__=='__main__':
    print(encrypt('ABC d',27))
    rint(decrypt('bcd e',1))
    print(crack(encrypt('It was the best of times, it was the worst of times.',15)))
