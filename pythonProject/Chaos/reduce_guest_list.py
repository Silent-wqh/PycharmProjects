list_guests = ['欧文亚隆', '薛涵', '爱因斯坦', '苏格拉底', '马克思', '尼采']
print('因为新购买的餐桌无法及时送达，因此只能邀请两人')
message = '，我很抱歉无法邀请你来共进晚餐'
print(list_guests.pop(0) + message)
print(list_guests.pop(0) + message)
print(list_guests.pop(0) + message)
print(list_guests.pop(2) + message)
print(list_guests[0] + '和'+ list_guests[1] + '依然被邀请共进晚餐')
del list_guests[0]
del list_guests[0]
print(list_guests)