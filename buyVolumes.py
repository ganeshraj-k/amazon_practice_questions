from typing import List

def buyVolumes( volumes: List[int]) -> List[List[int]]:
    listvols = []
    volsowned = 0
    currstk = []
    for vol in volumes:
        buy = []
        
        currstk.append(vol)
        
        currstk.sort()



        to_remove = []
        for volinstock in currstk:
           
            if volsowned+1 == volinstock:

                print(currstk, volsowned)
                buy.append(volinstock)
        #         print(currstk)
                volsowned+=1
                to_remove.append(volinstock)
        if not buy:
            listvols.append([-1])
        else:
            listvols.append(buy)
        currstk = list(set(currstk) - set(to_remove))

    return listvols
                
    


list_in =[1, 4, 3, 2, 5]

print(buyVolumes(list_in))
