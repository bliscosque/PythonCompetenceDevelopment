for _ in range(int(input())):
    c=int(input())
    votes=[]
    for _ in range(c):
        votes.append(int(input()))
    svotes=sum(votes)
    mvotes=max(votes)
    cmaxvotes=votes.count(mvotes)
    if cmaxvotes>1:
        print("no winner")
    else:
        if mvotes>svotes//2:
            print(f"majority winner {votes.index(mvotes)+1}")
        else:
            print(f"minority winner {votes.index(mvotes)+1}")
    