'''task: there is 35 heads and 94 legs among roadrunners and coyotes, how many roadrunners and coyotes do we have'''
rheads = 1
cheads = 1
rlegs = 2
clegs = 4
heads = 35
legs = 94

for x,y in (heads):
    x*rheads + y*cheads = heads
    print(x, y)
for x,y in (legs):
    x*rlegs + y*clegs = legs
    print(x, y)
