#!/usr/bin/env python

import pygtk
import gtk


def clicada(botao, label):
    if label.get_text() == "":
        label.set_text("obrigado")
    else:
        label.set_text("")

win = gtk.Window()
win.set_title('Regis')

win.set_size_request(300, 70)
win.connect("destroy", gtk.main_quit)

box = gtk.VBox()
win.add(box)

label = gtk.Label("")
box.pack_start(label)

botao = gtk.Button("clique-me")
box.pack_start(botao)
botao.connect("clicked", clicada, label)

win.show_all()
gtk.main()
