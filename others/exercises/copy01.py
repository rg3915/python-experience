#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import shutil

arq = open('lista.txt', 'r')
valor_linha = ''
dir_arquivo = ''

for linha in arq:

    valor_linha = linha.rstrip()
    dir_arquivo = os.path.dirname(valor_linha)

    if not os.path.exists(dir_arquivo):
        os.makedirs(dir_arquivo)

    shutil.copy2(valor_linha, '/arquivos/' + valor_linha)


arq.close()

# https://gist.github.com/1156757
