
from users import media_users
from send_email import send_verification_email

facebook_users = []
for user in media_users:
    if user['title'].lower() == "student":
        send_verification_email("support@debo.org",user['email'],"Student registration date will be on")
        # facebook_users.append(user)
# print(facebook_users)

