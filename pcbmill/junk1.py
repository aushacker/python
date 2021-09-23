def initInputs(intList):
    cmds = []
    for i in intList:
        pid = 'di' + str(i)
        cmds.append({pid + 'mo' : 0})
        cmds.append({pid + 'ac' : 2})
        cmds.append({pid + 'fn' : 1})
    return cmds

cmds = initInputs([1])

for c in cmds:
    print c
