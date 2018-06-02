'''task: there is 35 heads and 94 legs among roadrunners and coyotes, how many roadrunners and coyotes do we have'''

def solver (heads,legs):
    for roadrunner in range(heads+1):
        coyote = heads - roadrunner
        if(coyote*4 + roadrunner*2 == legs):
            return(roadrunner, coyote)
solutions = solver(35,94)
print(solutions)