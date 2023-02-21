import data.sign as sign

def lexer(text):
    code=[]
    for i in text:
        code.append(sign.check(i))
    print(code)