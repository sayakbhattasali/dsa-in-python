"""9. Team Game
N games are played between Team A and Team B. For every game, the winner is represented by
a character:
'A' means Team A won.
'B' means Team B won.
Count the number of wins for both teams and determine the overall winner. If both teams have
the same number of wins, print Draw.
Example:
Input:
5
BABBA
Output:
Team B
Explanation:
Team A wins 2 games and Team B wins 3 games."""

class Solution:
    def TeamGame(self,S):
        new={"A":0,"B":0}
        for char in S:
            if char in new:
                new[char]=new[char]+1
        if new["A"] > new["B"]:
            return "Team A"
        elif new["B"] > new["A"]:
            return "Team B"
        else:
            return "Draw"
    
N=int(input())
S=str(input())[:N]
obj=Solution()
result=obj.TeamGame(S)
print(result)



    
