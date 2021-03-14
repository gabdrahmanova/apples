def hat(player):
    return player[0]*player[1]+player[2]
# ivan=[6,10,8]
# igor=[7,7,7]
# score1=hat(ivan)
# score2=hat(igor)
# print('ivan',score1)
# print('igor',score2)
players=['ivan','igor','alex','valentin']
# carbs=[[6,10,8],[7,7,7],[7,8,9],[1,2,3]]
# score=[0,0,0,0]
# for i in range(4):
#     score[i]=hat(carbs[i])
#     print(players[i],score[i])
# players=[]
# for i in range(4):
#     players.append(input())
carbs=[[6,10,8],[7,7,7],[7,8,9],[1,2,3]]
score=[0,0,0,0]
file4=open('tetx.txt','w')
for i in range(4):
    score[i]=hat(carbs[i])
    print(players[i],score[i])
    file4.write(players[i])
    file4.write((str(score[i]))+'\n')
file4.close()

    