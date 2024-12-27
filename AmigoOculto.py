import random
import os
from EmailSender import send_email


def get_emails(file_name="emails.txt"):
    my_list = []
    with open(file_name) as f:
        for line in f:
            chunks = line.split(",")
            my_list.append((" ".join(chunks[:-1]), chunks[-1][:-1]))

    return my_list


def get_gifts(gifts, file_name="gifts.txt"):
    with open(file_name) as f:
        for line in f:
            chunks = line.split(",")
            gifts[" ".join(chunks[:-1])] = chunks[-1][:-1]
    return


def acceptable(participants, target):
    for i in range(len(participants)):
        if participants[i] == target[i]:
            return False
    return True


def simulate(my_list):
    shuffled_list = my_list
    for _ in range(7):
        shuffled_list = random.sample(shuffled_list, len(shuffled_list))
    while not acceptable(my_list, shuffled_list):
        shuffled_list = random.sample(my_list, len(my_list))
    result = {my_list[i]: shuffled_list[i] for i in range(len(my_list))}
    return result


def simulate_no_cycle(my_list, N=7):
    shuffled_list = my_list
    for _ in range(N):
        shuffled_list = random.sample(shuffled_list, len(shuffled_list))

    result = {
        shuffled_list[i]: shuffled_list[i + 1] for i in range(len(shuffled_list) - 1)
    }
    result[shuffled_list[-1]] = shuffled_list[0]

    return result


def broadcast(result):
    password = os.environ["EMAIL_OLIVEIRA_AUTH"]
    for src, tgt in result.items():
        name_dest, email_receiver = src[0], src[1]
        name_tgt = tgt[0]
        text = f"Prezado(a) {name_dest},\nSeu amigo oculto é: {name_tgt}! Compre algo legal para ele(a) :)\nValor sugerido: 80 - 100 reais.\nFeliz Natal! 🌟 ⛄ 🎅 🎄\n\nAtt.\n"
        # \nNa lista de desejos o seu/sua amigo(a) secreto colocou: {gifts.get(name_tgt, 'N/A')}.
        send_email(email_receiver=email_receiver, email_password=password, body=text)
    return


if __name__ == "__main__":
    my_list = get_emails()
    result = simulate(my_list)
    flag = input("Send emails? [y/n]")
    if flag == "y" or flag == "Y":
        broadcast(result)
    print("Done!")
