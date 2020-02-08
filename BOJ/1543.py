doc, query = input(), input()
cnt = 0
i=0
while(i+len(query) <= len(doc)):
    if doc[i:i+len(query)]==query:
        cnt += 1
        i = i+len(query)
    else: i+=1

print(cnt)