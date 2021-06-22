unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户，直到没有未验证的用户为止
#  将每个经过验证的用户都移到已验证的用户列表中
while unconfirmed_users:
    confirmed_user = unconfirmed_users.pop()

    print(f"Verifying user: {confirmed_user.title()}")
    confirmed_users.append(confirmed_user)

# 显示所有已验证的用户
print("\nThe following user have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
