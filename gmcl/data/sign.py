sign = {
    "leftParenthesis":["lps","("],
    "rightParenthesis":["rps",")"],
    "quotationMark":["qmk","\""],
    "leftBrace":["lbe","{"],
    "rightBrace":["rbe","}"],
    "multiplication":["mul","*"],
    "period":["per","."]
}
def check(text):
    for i in sign:
        if text == sign[i][1]:
            return f"{sign[i][0]}"  
    try:
        int(text)
        return f"int:{text}"
    except:
        return f"str:{text}"