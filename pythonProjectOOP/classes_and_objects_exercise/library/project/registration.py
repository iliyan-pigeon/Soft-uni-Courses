class Registration:
    def add_user(self, user, library):
        if user.user_id not in [u.user_id for u in library.user_records]:
            library.user_records.append(user)
        else:
            return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user, library):
        if user in library.user_records:
            library.user_records.remove(user)
        else:
            "We could not find such user to remove!"

    def change_username(self, user_id, new_username, library):
        for u in library.user_records:
            if user_id == u.user_id:
                if u.username != new_username:
                    old_name = u.username
                    u.username = new_username
                    if old_name in library.rented_books:
                        library.rented_books[u.username] = library.rented_books[old_name]
                        del library.rented_books[old_name]
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                return "Please check again the provided username - it should be different than the username used so far!"
        return f"There is no user with id = {user_id}!"


