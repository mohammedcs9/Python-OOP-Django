def info(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])

def Info(*args):
    print(args[0])
    print(args[1])
info(age=22, name="mohmd", phone=4846651) 
Info(22, "mohmd", 4846651)    