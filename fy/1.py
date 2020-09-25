p = input ('（加密）请输入一串英文字符：')
k = input ('请输入偏移量：')
for x in p :
    #while  k != "" and p !="":
       
        if  'a'<=x<='z':
           print(chr(ord('a')+(ord(x)-ord('a')+ord(k))%26),end="")
        elif  'A'<=x<='Z':
           print(chr(ord('A')+(ord(x)-ord('A')+ord(k))%26),end="")
        else:
           print(x,end="")
              

pt = input  ('\n（解密）请输入一串英文字符：')
k = input ('请输入偏移量：')
for x in pt :
   # while   k != "" and p !="":
       
        if 'a'<=x<='z':
           print(chr(ord('a')+(ord(x)-ord('a')-ord(k))%26),end="")
        elif 'A'<= x <='Z' :
           print(chr(ord('A')+(ord(x)-ord('A')-ord(k))%26),end="")
        else:
           print(x,end="") 
input()
        