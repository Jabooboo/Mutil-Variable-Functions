def solver (heads,legs):
    for roadrunner in range(heads+1):
        coyote = heads - roadrunner
        if(coyote*4 + roadrunner*2 == legs):
            return roadrunner, coyote
    return "No Solutions"
solutions = solver(35,94)
print(solutions)