import random
import os
from EmailSender import send_email

my_list = []
gifts = {}


def get_emails(my_list, file_name='emails.txt'):
    with open(file_name) as f:
        for line in f:
            chunks = line.split(',')
            my_list.append((' '.join(chunks[:-1]), chunks[-1][:-1]))
    return


def get_gifts(gifts, file_name='gifts.txt'):
    with open(file_name) as f:
        for line in f:
            chunks = line.split(',')
            gifts[' '.join(chunks[:-1])] = chunks[-1][:-1]
    return


get_emails(my_list)

get_gifts(gifts)


def acceptable(participants, target):
    for i in range(len(participants)):
        if participants[i] == target[i]:
            return False
    return True


def simulate(my_list=my_list):
    shuffled_list = random.sample(my_list, len(my_list))
    while not acceptable(my_list, shuffled_list):
        shuffled_list = random.sample(my_list, len(my_list))
    result = {my_list[i]: shuffled_list[i] for i in range(len(my_list))}
    return result


def broadcast(result):
    password = os.environ['EMAIL_OLIVEIRA_AUTH']
    for src, tgt in result.items():
        name_dest, email_receiver = src[0], src[1]
        name_tgt = tgt[0]
        text = f"Prezado(a) {name_dest},\nSeu amigo oculto é: {name_tgt}! Compre algo legal para ele(a) :)\nValor sugerido: 50 - 100 reais.\nNa lista de desejos o seu/sua amigo(a) secreto colocou: {gifts.get(name_tgt, 'N/A')}.\nFeliz Natal! 🌟 ⛄ 🎅 🎄\n\nAtt.\n"
        send_email(email_receiver=email_receiver,
                   email_password=password, body=text)
    return


if __name__ == '__main__':
    result = simulate()
    flag = input('Send emails? [y/n]')
    if flag == 'y' or flag == 'Y':
        broadcast(result)
    print('Done!')
