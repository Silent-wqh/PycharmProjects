list_guests = ['薛涵', '苏格拉底', '毛']
message = '我可以邀请你一起共进晚餐吗？'
print(list_guests[0] + ',' + message)
print(list_guests[1] + ',' + message)
print(list_guests[2] + ',' + message)
print(list_guests[2] + '无法赴约')
list_guests.pop()
list_guests.append('马克思')
print(list_guests[0] + ',' + message)
print(list_guests[1] + ',' + message)
print(list_guests[2] + ',' + message)
