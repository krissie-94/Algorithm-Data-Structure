class Solution:
  def hasPath(self, maze, start, destination):
    stack=[start]
    n,m=len(maze),len(maze[0])
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    stopped=set()

    while stack:
      r, c = stack.pop(0)
      if [r,c] == destination:return True
      
      for dr, dc in dirs:
        nwR,nwC =  r, c
        
        while 0 <= nwR+dr <= n-1 and 0 <= nwC+dc <= m-1 and maze[nwR+dr][nwC+dc] == 0:
          nwR += dr
          nwC += dc        
        
        if (nwR,nwC) in stopped:continue
        else:
          stopped.add((nwR,nwC))
          stack.append([nwR, nwC])
          
    return False
maze1=[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start1=[0,4]
destinaton1=[4,4]
ans=Solution()
bfs1=ans.hasPath(maze1,start1,destinaton1)
print("First Test Case Result: ",bfs1)    
print()
maze2=[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
start2=[0,4]
destinaton2=[3,2]

bfs2=ans.hasPath(maze2,start2,destinaton2)
print("Second Test Case Result: ", bfs2)   
