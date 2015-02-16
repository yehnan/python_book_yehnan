

# Steve Howell
# http://wiki.python.org/moin/SimplePrograms

def queen(n):
    answers = [()]
    
    def under_attack(col, ans):
        return (col in ans or
               any([abs(col - x) == len(ans)-i 
                   for i,x in enumerate(ans)]))
            
    for row in range(n):
        answers = [ans + (col,)
                    for ans in answers
                    for col in range(n)
                    if not under_attack(col, ans)]
    return answers



