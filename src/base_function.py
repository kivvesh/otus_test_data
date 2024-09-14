def make_custom_users(users):
    custom_users = []
    for user in users:
        custom_users.append(
            {
                "name": user['name'],
                "gender": user['gender'],
                "address": user['address'],
                "age": user['age'],
                "books": [],
            }
        )
    return custom_users
