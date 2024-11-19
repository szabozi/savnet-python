for i in range(10):
    if i % 2: continue
    print(i)
    if i % 10: break
else:
    print("error")
