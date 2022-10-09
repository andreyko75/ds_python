def group_gen(n=3):
    while True:
        for i in range(1, n + 1):
            yield i


def print_groups(users):
    for student, num_group in zip(users, group_gen(3)):
        print(student, 'in group ', num_group)


users = ['Smith J.', 'Petrova M.', 'Lubimov M.', 'Holov J.']
print_groups(users)
