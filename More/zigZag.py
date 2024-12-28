import time, sys
indent = 0
charOne = ">"
charTwo = "<"
increasingIndent = True

try: 
    while True:
        print(" " * indent,end="")
        time.sleep(0.1)
        

        if increasingIndent:            
            print(charOne*indent)
            indent = indent + 1 # Moving right
            if indent == 20: 
                increasingIndent = False

        else:            
            print(charTwo*indent)
            indent = indent - 1 # Moving Left
            if indent == 0:
                increasingIndent = True
    
except KeyboardInterrupt:
    sys.exit() 