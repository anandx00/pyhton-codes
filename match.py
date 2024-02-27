def tally(rows):
   team="Team                           | MP |  W |  D |  L |  P"
   match_played=0
   win=0
   draw=0
   loss=0
   point=0
   print (team)
   for i in rows:
      data=i.split(';')
      if data[-1]=='win':
         print(data[0]," "*(29-len(data[0])),f'|  {match_played+1} |  {win+1} |  {draw} |  {loss} |  {point +3}')
         print(data[1]," "*(29-len(data[0])),f'|  {match_played+1} |  {win} |  {draw} |  {loss+1} |  {point}')
      if data[-1]=='loss':
         print(data[0]," "*(29-len(data[0])),f'|  {match_played+1} |  {win} |  {draw} |  {loss+1} |  {point}')
         print(data[1]," "*(29-len(data[0])),f'|  {match_played+1} |  {win+1} |  {draw} |  {loss} |  {point}')
      if data[-1]=='draw':
         print(data[0]," "*(29-len(data[0])),f'|  {match_played+1} |  {win} |  {draw} |  {loss} |  {point+1}')
         print(data[1]," "*(29-len(data[0])),f'|  {match_played+1} |  {win} |  {draw} |  {loss} |  {point+1}')
tally(["Allegoric Alaskans;Blithering Badgers;draw","Allegoric Alaskans;Blithering Badgers;draw"])