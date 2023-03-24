import lexer.lexer as lexer

while True:
    try:
        text = input("InterpreterCode:newkinisGMCL> ")
        if text == "stopCode":break
        lexer.lexer(text)
    except:print("InterpreterError : pythonError")