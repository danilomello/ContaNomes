#Testa o módulo contaCaraacteres

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import contaCaracteres

nome = "Danilo Mello"
contaCaracteres.contarCaracteres(nome)
