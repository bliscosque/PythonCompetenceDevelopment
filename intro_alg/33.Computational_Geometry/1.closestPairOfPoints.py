# implemented from stanford course - 03_III._DIVIDE__CONQUER_ALGORITHMS_Week_1

import math

# calculate distance from p1 and p2
def distance(p1,p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def closest_pair(pts):
    def closest_pair_rec(p_sorted_x,p_sorted_y):
        # 3 or less points = brute force - BASE CASE
        if len(p_sorted_x)<=3:
            return brute_force(p_sorted_x)
    
        mid=len(pts_sorted_x)//2
        left_x,right_x=p_sorted_x[:mid],p_sorted_x[mid:]

        midpoint=pts_sorted_x[mid][0]
        
        #list for y for 2 half
        left_y=list(filter(lambda pt: pt[0] <= midpoint, pts_sorted_y))
        right_y=list(filter(lambda pt: pt[0] > midpoint, pts_sorted_y))

        # closest pair in 2 half
        (d1,pair1)=closest_pair_rec(left_x,left_y)
        (d2,pair2)=closest_pair_rec(right_x,right_y)
        d_min=min(d1,d2)
        closest_pair = pair1 if d1 < d2 else pair2

        # closest pair that crosses the division line
        (d3,pair3)=closest_split_pair(pts_sorted_x,pts_sorted_y,d_min)

        if d3<d_min:
            return (d3,pair3)
        else:
            return (d_min,closest_pair)

    # Find closest split pair that crosses middle line
    def closest_split_pair(pts_sorted_x,pts_sorted_y,d_min):
        # find points within crossing line plus/minus d_min
        mid_x=pts_sorted_x[len(pts_sorted_x)//2][0]
        strip=[p for p in pts_sorted_y if mid_x - d_min <= p[0] <= mid_x + d_min] 

        min_dst=d_min
        closest_pair=None
        for i in range(len(strip)):
            for j in range(i+1,min(i+7, len(strip))): #we need to check 7 pts at maximum... this is the dificult part, to PROVE this
                p,q=strip[i],strip[j]
                dst=distance(p,q)
                if dst<min_dst:
                    min_dst=dst
                    closest_pair=(p,q)
        return (min_dst,closest_pair)
        
    def brute_force(pts):
        min_dst=float('inf')
        closest_pair=None
        n=len(pts)
        for i in range(n):
            for j in range(i+1,n):
                dst=distance(pts[i],pts[j])
                if dst<min_dst:
                    min_dst=dst
                    closest_pair=(pts[i],pts[j])
        return (min_dst,closest_pair)
    
    pts_sorted_x=sorted(pts, key=lambda point:point[0])
    pts_sorted_y=sorted(pts, key=lambda point:point[1])
    return closest_pair_rec(pts_sorted_x,pts_sorted_y)


pts = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
dst,pair=closest_pair(pts)
print(f"Closest pair: {pair}, distance: {dst}")
