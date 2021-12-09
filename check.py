# Este programa assume que sua solucao para o trabalho 2
# fica no arquivo chamado "solution.py".
# Modifique a linha abaixo para usar outro nome de arquivo:

nome_do_programa = 'trabalho2.py'

import os

t = 0
while True:
    t += 1
    in_file = f'TestCases/{t:02d}_in.txt'
    res_file =f'Tmp/{t:02d}_out.txt'
    out_file =f'TestCases/{t:02d}_out.txt'

    if os.path.exists(in_file):
        print(out_file)
        os.system('python ' + nome_do_programa + ' < ' + in_file + ' > ' + res_file)
        os.system('diff ' + res_file + ' ' + out_file)
    else:
        break
