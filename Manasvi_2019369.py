"""
CSE101: Introduction to Programming
Assignment 3

Name        :Manasvi Singh
Roll-no     :2019369
"""



import math
import random



def dist(p1, p2):
    """
    Find the euclidean distance between two 2-D points

    Args:
        p1: (p1_x, p1_y)
        p2: (p2_x, p2_y)
    
    Returns:
        Euclidean distance between p1 and p2
    """
   
    distance_between=((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)
    return distance_between



def sort_points_by_X(points):
    """
    Sort a list of points by their X coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by X coordinate
    """
  
    
    
    points.sort()
    return points
    



def sort_points_by_Y(points):
    """
    Sort a list of points by their Y coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by Y coordinate 
    """
    

    
    points.sort(key = lambda a: a[1])
    
    return points  
  



def naive_closest_pair(plane):
    """
    Find the closest pair of points in the plane using the brute
    force approach

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    if(len(plane)>=2):
        P1=plane[0]
        P2=plane[1]
        dmin=dist(P1,P2)
   
        length=len(plane)
        for i in range(length):
            for j in range(i+1,length):
                d=dist(plane[i],plane[j])
                if(d<dmin):
                    dmin=d
                    P1=plane[i]
                    P2=plane[j]
        return [dmin,P1,P2]





def closest_pair_in_strip(points, d):
    """
    Find the closest pair of points in the given strip with a 
    given upper bound. This function is called by 
    efficient_closest_pair_routine

    Args:
        points: List of points in the strip of interest.
        d: Minimum distance already found found by 
            efficient_closest_pair_routine

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)] if
        distance between p1 and p2 is less than d. Otherwise
        return -1.
    """
    sortedbyy=sort_points_by_Y(points)
    n=len(sortedbyy)
    e=-1
    C=0
    for i in range(n):
        for j in range(i+1,n):
            if (sortedbyy[i][1]-sortedbyy[j][1])<d:
                DISTANCE=dist(sortedbyy[i],sortedbyy[j])
                if(DISTANCE<d):
                    d=DISTANCE
                    POINT1=sortedbyy[i]
                    POINT2=sortedbyy[j]
                    e=e+1
    if(e==-1):
        return -1
    else:
        return [d,POINT1,POINT2]
            
            
            
    




def efficient_closest_pair_routine(points):
    """
    This routine calls itself recursivly to find the closest pair of
    points in the plane. 

    Args:
        points: List of points sorted by X coordinate

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    listelementsstrip=[]
    j=0
    N=len(points)
    XMIDDLE=points[N//2]
    
    if len(points)<=2:
        if len(points)==2:
            return [dist(points[0],points[1]),points[0],points[1]]
        elif len(points)==1:
            return [math.inf,0,0]
    
    
    XL=points[:N//2]
    XR=points[(N//2):]
    dlmin=efficient_closest_pair_routine(XL)
    drmin=efficient_closest_pair_routine(XR)
    DMIN=min(dlmin[0],drmin[0])
    if(DMIN==dlmin[0]):
        POINT1=dlmin[1]
        POINT2=dlmin[2]
    else:
        POINT1=drmin[1]
        POINT2=drmin[2]
    """DMIN is smaller of the two distances in the two planes being compared"""
    for m in points:
        
        diff=abs(m[0]-XMIDDLE[0])
        if(diff<DMIN):
            listelementsstrip=listelementsstrip+[m]
            
    DSTRIP=closest_pair_in_strip(listelementsstrip,DMIN)
    if(DSTRIP==-1):
         return [DMIN,POINT1,POINT2]
    else:
        return DSTRIP







def efficient_closest_pair(points):
    """
    Find the closest pair of points in the plane using the divide
    and conquer approach by calling efficient_closest_pair_routine.

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    DFIN=efficient_closest_pair_routine(sort_points_by_X(points))
    return DFIN


def generate_plane(plane_size, num_pts):
    """
    Function to generate random points.

    Args:
        plane_size: Size of plane (X_max, Y_max)
        num_pts: Number of points to generate

    Returns:
        List of random points: [(p1_x, p1_y), (p2_x, p2_y), ...]
    """
    
    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i%plane_size[0] + 1, i//plane_size[1] + 1) for i in gen]

    return random_points



if __name__ == "__main__":  
    #number of points to generate
    num_pts = 10
    #size of plane for generation of points
    plane_size = (10,10) 
    plane = generate_plane(plane_size, num_pts)
    
    
    print(plane)
    print("Closest pair by naive pair routine ")
    print("Closest pair  ",end=" ")
    print(naive_closest_pair(plane)[1:])
    
    print("Distance",end=" ")
    print(round(naive_closest_pair(plane)[0],1))
    
    print("Closest pair by divide and conquer algorithm ")
    print("Closest pair  ",end=" ")
    print(efficient_closest_pair(plane)[1:])
    
    print("Distance",end=" ")
    print(round(efficient_closest_pair(plane)[0],1))
    

   
    
