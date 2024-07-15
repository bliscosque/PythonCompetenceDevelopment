def sched(activities):
    activities.sort(key=lambda x:x[1])

    scheduled=[]
    last_end_time=0

    for start,end in activities:
        if start >= last_end_time:
            scheduled.append((start,end))
            last_end_time=end

    return scheduled

activities=[(1,3),(2,5),(3,9),(6,8)]
print(sched(activities))