import unittest
from AmigoOculto import acceptable, get_emails, get_gifts, acceptable, simulate


class TestAmigoOculto(unittest.TestCase):
    def test_get_emails(self):
        email_list = [('João', 'joao@gmail.com'),
                      ('Manoel', 'manoel@gmail.com'),
                      ('Maria Amelia', 'amelia@gmail.com'),]
        emails = []
        get_emails(emails, file_name='test_emails.txt')
        self.assertEqual(email_list, emails)

    def test_get_gifts(self):
        gift_list = {'João Henrique': 'camisa regata', 'Manoel': 'Loção pós barba',
                     'Maria Amelia': 'camisetas branca Hering decote V (tamanho: P)'}
        gifts = {}
        get_gifts(gifts, 'test_gifts.txt')
        self.assertEqual(gift_list, gifts)

    def test_acceptable(self):
        participants = ['João', 'Manoel', 'Maria Amelia']
        target = ['Manoel', 'Maria Amelia', 'João']
        self.assertTrue(acceptable(participants, target))

    def test_not_acceptable(self):
        participants = ['João', 'Manoel', 'Maria Amelia']
        target = ['Manoel', 'João', 'Maria Amelia']
        self.assertFalse(acceptable(participants, target))

    def test_simulate(self):
        participants = ['João', 'Manoel', 'Maria Amelia']
        result = simulate(participants)
        self.assertNotEqual(participants, result)
