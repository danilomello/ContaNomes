#! python3

'''
Este script testa o módulo contaCaraacteres
'''

import unittest
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
import contaCaracteres

class contaCaracteresTest(unittest.TestCase):
    
    def test_qntLetrasNome(self):
        nome = "Danilo Mello"
        self.assertEqual(contaCaracteres.qntLetrasNome(nome), 12)

    def test_mostraMaiorNome(self):
        nomes = ["Danilo Mello", "João Silva", "Mariana Tester"]
        self.assertEqual(contaCaracteres.mostraMaiorNome(nomes), 14)

if __name__ == '__main__':
    unittest.main()
