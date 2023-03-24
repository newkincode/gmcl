import data.sign as sign

def lexer(text):
    code=[]
    for i in text:
        code.append(sign.check(i))
    print(code)
    for i in code:
        if i  == "lps":
            try:
                if "str" in code[code.index(i)-1] and "rps" in code[code.index(i)+1]:
                    print("함수감지!")
            except:
                print("syntaxError : missingParentheses")