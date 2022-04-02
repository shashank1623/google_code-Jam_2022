n = int(input())
s = ""
for i in range(0, n):
    t = int(input())
    list_points = [int(s) for s in input().split(" ")]
    list_pos = [int(s) for s in input().split(" ")]
    result_string = f"Case #{i+1}: "
    max_pos = max(list_pos)
    list_points.insert(0,0)
    list_pos.insert(0,0)
    list_path = []
    max_rs = 0
    max_rs1 = 0
    #path creator 
    for j in range(max_pos+1,t+1):
        path = []
        if list_pos[j] == 0:
            max_rs += list_points[j]
        else:
            path.append(j)
            if list_pos[j] == 1:
                path.append(1)
                list_path.append(path)
            else:
                k = list_pos[j]
                while k != 1:
                    path.append(k)
                    k = list_pos[k]
                    if k == 1:
                        path.append(k)
                        break
                list_path.append(path)
            
    del list_pos
    pass_p = {}

    #calculator  
    for x,p in enumerate(list_path):
        for i in range(len(list_path)):
            pass_p[i] = False
        pass_p[x] = True
        sum = max_rs
        block = {}
        for i in range(t+1):
            block[i] = False
        max_t = 0
        for j in p:
            block[j] = True
            max_t = max(max_t,list_points[j])
        sum += max_t
        for v,p1 in enumerate(list_path):
            if pass_p[v]:
                continue
            else :
                max_t = 0
                for j in p1:
                    if not block[j]:
                        max_t = max(max_t,list_points[j])
                        block[j] = True
                sum += max_t
        max_rs1 = max(max_rs1,sum)
    result_string += f"{max_rs1}"
    print(result_string)
