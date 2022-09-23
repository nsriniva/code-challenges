#input: [2,8,7,0,-1,-5,3,-2]
#output: 2, -2

#input: [13,1,4,6,-2,-9,-20]
#output: -2, 1

from collections import defaultdict
def near_zero(ilist):
    diffd =  defaultdict(list)
    
    for idx,n  in enumerate(ilist):
        for m in ilist[idx+1:]:
            diffd[abs(n+m)].append((n,m))
            
    sdiff = sorted(diffd.items(), key = lambda x:x[0])
    
    #print(sdiff)
    
    return sdiff[0][1][0]
    
def near_zero3(ilist):

    ilist_sort = sorted(ilist, key=lambda x: abs(x))
    
    lrsum_func = lambda x: abs(ilist_sort[x]+ilist_sort[x+1])

    lilist = len(ilist)    
    
    lrsum = lrsum_func(0)
    idx = 1 
    while idx <= lilist-2:
        if (lrsum_t := lrsum_func(idx)) <= lrsum:
            lrsum = lrsum_t
            idx += 1
        else:
            break

    return (ilist_sort[idx-1], ilist_sort[idx])
    
def near_zero2(ilist):

    ilist_sort = sorted(ilist)
    lrsum_func = lambda l,r: ilist_sort[l]+ilist_sort[r]
        
    tlidx = 0
    tridx = len(ilist) - 1
    
    while tlidx < tridx:
        lidx = tlidx
        ridx = tridx
        lrsum = lrsum_func(lidx, ridx)
                
        if lrsum > 0:   
            tridx -= 1
        elif lrsum < 0:
            tlidx += 1
        else:
            break
               
        
    ret = (ilist_sort[lidx], ilist_sort[ridx])
            
    return ret          
        
test_vecs = [
    ([2,8,7,0,-1,-5,3,-2], (-2,2)),
    ([13,1,4,6,-2,-9,-20], (-2,1))
]

if __name__ == '__main__':
    for tv in test_vecs:
        assert sum(near_zero(tv[0])) == sum(tv[1])
        assert sum(near_zero2(tv[0])) == sum(tv[1])
        assert sum(near_zero3(tv[0])) == sum(tv[1])
