current_users = ['admin', 'aa', 'bb', 'cc', 'Dd']
new_users = ['CC', 'dD', 'ee', 'ff', 'gg']
current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'用户名"{new_user}"已存在，请使用其他用户名')
    else:
        print(f'用户名"{new_user}"未被使用')