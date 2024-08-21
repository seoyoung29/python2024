def p(space,space_num,*args): #arguments ,인수
    str=args(0)
    for i in range(1,len(args)):
        str=str+args[i]
        print(str)


p(',',3,'😊','💕','🔜')
p('t','z','y','x','f')