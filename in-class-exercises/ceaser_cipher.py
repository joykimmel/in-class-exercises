import numpy as np

def ceaser():

    decode = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M', '?':'?', '!':'!', '.':'.'}
    
    
    usr_input = raw_input("Please enter phrase to decode: ")
    
    answer = ""
    
    for i in usr_input:
        if decode.get(i) == None:
            answer = answer + " "
        else:
            answer = answer + "%s" % (decode.get(i))
    
    print answer
    
    usr_input2 = raw_input("Please enter phrase to encode: ")
    
    encode = {y:x for x,y in decode.iteritems()}
    
    answer2 = ""
    for i in usr_input2:
        if encode.get(i) == None:
            answer2 = answer2 + " "
        else:
            answer2 = answer2 + "%s" % (encode.get(i))
    
    
    print answer2


ceaser()
