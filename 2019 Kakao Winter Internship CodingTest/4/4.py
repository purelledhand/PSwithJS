def solution(k, room_number):
    dht = {}
    assign = []

    for i in room_number:
        target = i
        visited = [target]
        while dht.get(target) is not None:
            print(dht[target], dht)
            target = dht[target]
            visited.append(target)
        for j in visited:
            dht[j] = target+1
        assign.append(target)

    print(assign)
        
    return assign

solution(10, [1,3,4,1,3,1])

'''
DHT 원리로 풀이
'''