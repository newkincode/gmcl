import lexer.lexer as lexer

while True:
    try:
        text = input("InterpreterCode:newkinisGMCL> ")
        if "exit code=" in text:
            print("exit code",text.replace("exit code=", ""))
            break
        lexer.lexer(text)
    except:print("InterpreterError : pythonError")