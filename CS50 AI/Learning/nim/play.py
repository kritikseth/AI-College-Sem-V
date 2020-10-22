from nim import train, play

ai = train(10)
play(ai)

for i in range(100000000):
    flag = i

ai = train(1000)
play(ai)
