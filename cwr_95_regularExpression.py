import re
pattern=r"[cdew]+yclone"
text='''Sport cyclone is a form of physical activity or game.[1] Often competitive
 and organized, sports use, maintain, or improve physical ability and skills.
   They also provide enjoyment to participants and, in some cases, entertainment to spectators.[2] 
   Many sports exist, with different participant numbers, some are done by a single person with others being
     done by hundreds. Most sports take place either in teams or competing as individuals. 
     Some sports allow dyclone a "tie" or "draw", in which there is no single winner; 
     others provide tie-breaking methods to ensure one winner. 
     A number of contests may be arranged in a tournament format, producing a champion. 
     Many sports leagues make an annual champion by arranging games in a regular sports season, 
     followed in some cases by playoffs.'''
#match=re.search(pattern,text)
matches=re.finditer(pattern,text)
#print(match)
for match in matches:
    #print(match.span())
    #print(type(match.span()))
    print(text[match.span()[0]:match.span()[1]])