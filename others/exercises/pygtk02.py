import gtk

janela = gtk.Window(gtk.WINDOW_TOPLEVEL)
janela.set_title("TreeView com Combo")
janela.connect("delete_event", gtk.main_quit)

modelo = gtk.ListStore(str)
modelo.append(['Cartucho de Impressora'])
modelo.append(['Computador 486 Semi-Novo'])
modelo.append(['Computador Top de Linha'])
modelo.append(['Monitor 21"'])
modelo.append(['Mouse Ps2'])
modelo.append(['Teclado ABNT2'])
modelo.append(['Impressora LX-300L'])

combo = gtk.CellRendererCombo()
combo.set_property("model", modelo)
combo.set_property('text-column', 0)
combo.set_property('editable', True)

barra = gtk.CellRendererProgress()

tGrade = gtk.TreeView()
mgrade = gtk.ListStore(str, str, str, str, str, int)
tGrade.set_model(mgrade)
coluna1 = gtk.TreeViewColumn("Ordem", gtk.CellRendererText(), text=0)
coluna2 = gtk.TreeViewColumn("Produto", combo, text=1)
coluna3 = gtk.TreeViewColumn("Valor", gtk.CellRendererText(), text=2)
coluna4 = gtk.TreeViewColumn("Qtd", gtk.CellRendererText(), text=3)
coluna5 = gtk.TreeViewColumn("Total", gtk.CellRendererText(), text=4)
coluna6 = gtk.TreeViewColumn("Ok", barra, value=5)
coluna1.set_resizable(True)
coluna2.set_resizable(True)
coluna3.set_resizable(True)
coluna4.set_resizable(True)
coluna5.set_resizable(True)
coluna2.set_expand(True)
coluna1.set_sort_column_id(0)
coluna2.set_sort_column_id(1)
coluna3.set_sort_column_id(2)
coluna4.set_sort_column_id(3)
coluna5.set_sort_column_id(4)
tGrade.append_column(coluna1)
tGrade.append_column(coluna2)
tGrade.append_column(coluna3)
tGrade.append_column(coluna4)
tGrade.append_column(coluna5)
tGrade.append_column(coluna6)
# tGrade.get_selection().set_mode(gtk.SELECTION_SINGLE)
msg = '(escolha um produto)'
mgrade.append(['Qualquer', msg, '5.00', '2', '10.00', 10])
mgrade.append(['Outro', msg, '15.00', '22', '110.00', 30])


def on__combo__edited(renderer, path, new_text, model):
    coluna_produto = 1
    model[path][coluna_produto] = new_text

combo.connect("edited", on__combo__edited, mgrade)

janela.add(tGrade)
janela.show_all()
gtk.main()
