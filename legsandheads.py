'''task: there is 35 heads and 94 legs among roadrunners and coyotes, how many roadrunners and coyotes do we have'''

def solver (heads,legs):
    for roadrunner in range(heads):
        coyote = 35 - roadrunner
        if(coyote*4 + roadrunner*2 == legs):
            print('Coyotes = ', coyote,' ', 'Roadrunners = ', roadrunner)
    return

solver(35,94)