ler_user = []
with open('user_register.txt','r') as arquivo:
    for l in arquivo:
        ler_user.append(l.split(','))
for user in ler_user:
    if user[3].replace('\n', '') == 'None':
        print('oi') 