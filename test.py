# from tkinter import *
#
# root = Tk()
#
# def hide(choice):
#     if choice == "YES":
#         e.grid()
#     else:
#         e.grid_remove()
#
# field = ["YES",""]
# query_text = StringVar()
# lblname = Label(root, font=("arial", 10, "bold"), text="Query/Reply", bd=8, anchor="w")
# lblname.grid(row=0, column=0, sticky=W)
# txtname28 = OptionMenu(root, query_text, *field, command=hide)
# txtname28.grid(row=0, column=1, sticky=W)
#
# hidden_text = StringVar()
# hidden_text.set('Show this text?')
# e = Entry(root, font=("arial", 10, "bold"), bd=8, justify="left", textvariable = hidden_text)
# e.grid(row=0, column=2)
#
# root.mainloop()


# time_check = [False for idx in range(3)]
#
# print(time_check)

a = [False, False, False, True]

# print(a.index(True)+1)

print(a.count(False))