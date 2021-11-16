import math
def minmax(curdepth,nodeindex,maxplayer,scores,targetdepth):
  if(curdepth==targetdepth):
    return scores[nodeindex]
  if(maxplayer):
    return max((minmax(curdepth+1,nodeindex*2,False,scores,targetdepth)),(minmax(curdepth+1,nodeindex*2+1,False,scores,targetdepth)))
  else:
    return min((minmax(curdepth+1,nodeindex*2,True,scores,targetdepth)),(minmax(curdepth+1,nodeindex*2+1,True,scores,targetdepth)))
scores=[1,3,5,1,-6,-4,0,9]
targetdepth=math.log(len(scores),2)
print(minmax(0,0,True,scores,targetdepth))