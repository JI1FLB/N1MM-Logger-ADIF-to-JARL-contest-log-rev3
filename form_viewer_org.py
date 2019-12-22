import tkinter as tk

import os


# Main windows
root = tk.Tk()
root.title('form file Viewer')

def open_form() :
    fill_in_form = open( "form.txt" ,"r", encoding='utf-8')
    fill_in = fill_in_form.readlines()
    for fill in fill_in :
        fill = fill.lstrip('[')
        fill = fill.lstrip()
        fill = fill.rstrip(']')
        fill = fill.rstrip()
        text_widget.insert('end',fill+'\n')
    fill_in_form.close()


def save_form() :
    # form.txtファイルのバックアップを追加する。
    save_form = text_widget.get('1.0','end -1c')
    fill_in_form_new = open( "form.txt" ,"w", encoding='utf-8')
    fill_in_form_new.write( save_form )
    fill_in_form_new.close()
    # 表示情報の削除
    text_widget.delete('1.0','end')
    

def close_disp() :
    root.destroy()
    

text_widget = tk.Text(root)
text_widget.grid(column = 0, row = 0, sticky = (tk.N, tk.S, tk.E, tk.W))

root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight = 1)

#メニューバー作成 
men = tk.Menu(root) 

#メニューバーを画面にセット 
root.config(menu=men) 

#メニューに親メニュー（ファイル）を作成する 
menu_file = tk.Menu(root) 
men.add_cascade(label='ファイル', menu=menu_file) 

#親メニューに子メニュー（開く・閉じる）を追加する 
menu_file.add_command(label='Open', command=open_form) 
menu_file.add_separator()
menu_file.add_command(label='Save', command=save_form)
menu_file.add_separator() 
menu_file.add_command(label='close', command=close_disp)

root.mainloop()
