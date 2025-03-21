from StackClass import ArrayStack

def CheckBrackets(statement):
    stack = ArrayStack(100)
    for ch in statement:
        if ch in ('{','[', '('):
            stack.push(ch)
        elif ch in ('}', ']',')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch == '}' and left != "{") or \
                    (ch == ']' and left != "[") or \
                    (ch== ')' and left != "(") :
                    return False
    
    return stack.isEmpty()

''' 실행 코드
print(CheckBrackets("{A[(i+1)]=0;}"))
print(CheckBrackets("if ((x<0) && (y<3)"))
print(CheckBrackets("while (n<8)) {n++;}"))
print(CheckBrackets("arr[(i+1])=0;"))
'''