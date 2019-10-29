from django.test import TestCase
from django.core import mail 

class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name = 'Jessica Oliveira', cpf='12345678901', 
                    email='jessica@oliveira.net', phone='61-99854-8747')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = ('Confirmação de inscrição')
        self.assertEqual(expect, self.email.subject)
    
    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'
        self.assertEqual(expect, self.email.from_email)
    
    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'jessica@oliveira.net']
        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Jessica Oliveira',
            '12345678901',
            'jessica@oliveira.net',
            '61-99854-8747'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)        
