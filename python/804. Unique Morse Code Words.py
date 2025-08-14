from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
            hashmap={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
            
            seen = set()
            
            for word in words:
                temp = ''
                for char in word:
                    temp += hashmap[char]
                seen.add(temp)
                
            return len(seen)