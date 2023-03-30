# given a running stream of chats, output the first non-repeating char in the str formed so far. -1 if doesn't exist
from collections import deque
def nonRepChar(s):
    q=deque() # using as a queue
    freq=[0]*27

    for ch in s:
        q.append(ch)
        #print(ch, q)
        freq[ord(ch)-ord('a')]+=1

        while(len(q)>0):
            idx=ord(q[0])-ord('a')
            if freq[idx]>1:
                q.popleft()
            else:
                print(q[0])
                break
        if len(q)==0:
            print('-1')

nonRepChar('aabccbcd') # a -1 b b b -1 -1 d