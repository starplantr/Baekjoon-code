def solution(s):
    answer = True
    stack = []
    
    for i in range(len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            if stack[-1] == '(':
                if s[i] == ')':
                    stack.pop()
                else:
                    stack.append(s[i])
            
            else:
                stack.append(s[i])
            
    if len(stack) == 0:
        return True
    
    else: 
        return False