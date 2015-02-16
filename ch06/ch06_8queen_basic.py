

def queen(n):
    answers = []
    
    def is_safe(ans, col):
        for i, c in enumerate(ans):
            if len(ans)-i == abs(c-col):
                return False
        return True
        
    def sub(ans, n):
        if len(ans) == n:
            answers.append(ans)
        else:
            for col in range(n):
                if col not in ans and is_safe(ans, col):
                    sub(ans + (col,), n)
    
    sub((), n)
    return answers
