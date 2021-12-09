name_of_script = 'project.py'

import os

t = 0
while True:
    t += 1
    in_file = f'TestCases/{t:02d}_in.txt'
    res_file =f'Tmp/{t:02d}_out.txt'
    out_file =f'TestCases/{t:02d}_out.txt'

    if os.path.exists(in_file):
        print(out_file)
        os.system('python ' + name_of_script + ' < ' + in_file + ' > ' + res_file)
        os.system('diff ' + res_file + ' ' + out_file)
    else:
        break
