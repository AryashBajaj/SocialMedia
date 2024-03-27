from django.contrib.auth.models import User

#Script to names of all users. Rectifying a previous issue

users = User.objects.all()
for user in users :
    if user.first_name :
        continue
    username = user.username
    firstName, lastName = "", ""
    n = len(username)
    for i in range(n - 1, -1, -1) :
        if (username[i].isupper()) :
            lastName = username[i:]
            firstName = username[:i]
            break
    print(firstName + lastName)
    user.first_name = firstName
    user.last_name = lastName
    user.save()
