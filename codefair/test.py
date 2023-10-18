class User():
    def __init__(self, name=''):
        self.name = name
    def prinTest(self):
        return self.name
count = 0
users=[]
users.append(User("Abed"))
users.append(User("Abdi"))
print(len(users))

usernam = 'Abed'
if usernam in users:
    print('Yes')
else:
    print('No')