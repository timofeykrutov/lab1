from ClientGetID import ClientGetID
from ClientGetFriendsAges import ClientGetFriendsAges
from Gist import Gist
from random import randint


friends_id_arr = None
while friends_id_arr is None:
    input_username = input()

    friends_id_arr = ClientGetID(input_username).execute()

randomlist = list()
friends_ages = ClientGetFriendsAges(friends_id_arr).execute()

for i in range(0,50):
    randomlist.append(randint(1, 100))

if len(friends_ages) == 0:
    print('Нет друзей :(')
    input()
else:
    print("ID: ", friends_id_arr)
    print("Ages: ", friends_ages)

    Gist(randomlist).print_hist()
