from config import *
import modules.enc as enc
from tools import *

root = Tk()
root.geometry(str(win_w) + "x" + str(win_h)+ "+{}+{}".format(w_center_x, w_center_y))
root.iconbitmap("assets/ico.ico")
root.title("Passworder")
root['bg']="#000000"

def main():
	global inf, next_btn, back_btn, tablo, yes_btn, no_btn, cancel, qua, open_search_btn, inf_name

	run_line_1 = Label(root, text="   P A S S W O R D E R", font=((baseFont), "43"), bg="#000000", fg="#00FF00")
	run_line_1.place(x=line_x_1, y=2)

	run_line_2 = Label(root, text="   P A S S W O R D E R", font=((baseFont), "43"), bg="#000000", fg="#00FF00")
	run_line_2.place(x=line_x_2, y=2)

	version = Label(root, width=10, text=f"V {VERSION}", font=((baseFont), "18"), bg="#00FF00", fg="#000000")
	version.place(x=255, y=270)

	dev = Label(root, text="© ZERDICORP", font=((baseFont), "8"), bg='#000000', fg=fg)
	dev.place(x=win_w/2 - 38, y=win_h-15)

	def change_color():
	    global line_x_1, line_x_2, color

	    color_rnd = random.choice(color)
	    version["bg"]=color_rnd
	    run_line_1.place(x=line_x_1)
	    run_line_2.place(x=line_x_2)
	    line_x_1 -= 5
	    line_x_2 -= 5
	    if (line_x_2 < 0 and line_x_2 > -20):
	        line_x_1 = 600
	    if (line_x_1 < 0 and line_x_1 > -20):
	        line_x_2 = 600

	    root.after(100, change_color)

	change_color()

	# все сервисы
	open_search_btn = Button(root, text=" search ", fg="#FFDE00", bg="#363636", cursor="hand2", command=lambda: search())
	open_search_btn.place(x=10, y=0+add_height)

	qua = Label(root, width=16, height=1, text="", font=((baseFont), "12"), bg=fg_titles, fg="#FFFF00", borderwidth=1, relief="ridge")
	qua.place(x=66, y=0+add_height)

	all_service = Text(root, width=25, height=4, bg="#000000", fg=fg, cursor="hand2")
	all_service.bind("<Button-1>", lambda x: root.after(10, past_detail) if len(services) else 0)
	all_service.place(x=10, y=31+add_height)

	# имя сервиса
	service_name = Label(root, width=22, height=1, text="", font=((baseFont), "12"), bg=fg_titles, fg="#FFFF00", borderwidth=1, relief="ridge", cursor='hand2')
	service_name.bind("<Button-1>", lambda x: root.after(10, copy_name))
	service_name.place(x=220, y=0+add_height)

	# текстовое поле для отображения пароля и логина
	view_detail = Text(root, width=25, height=4, bg="#000000", fg=fg, cursor="hand2")
	view_detail.bind("<Button-1>", lambda x: root.after(10, copy_detail))
	view_detail.place(x=220, y=31+add_height)

	# поле для добавления сервисов
	inf_name = Label(root, text="", width=22, height=1, font=((baseFont), "12"), bg=fg_titles, fg="#FFFF00", borderwidth=1, relief="ridge")
	inf_name.place(x=10, y=111+add_height)

	# поле удаления
	Label(root, text="Delete", font=((baseFont), "13"), bg='#000000', fg=fg).place(x=10, y=296+add_height)
	del_line = Entry(root, font=((baseFont), "14"), width=32, bg=fg_titles, fg=fg)
	del_line.bind("<Return>", lambda x: del_s())
	del_line.bind("<Button-1>", lambda x: past_del())
	del_line.place(x=65, y=295+add_height)

	# console
	console = Label(root, text="", width=45, height=2, font=((baseFont), "12"), bg="#000000", fg=fg, borderwidth=1, relief="ridge")
	console.place(x=13, y=350+add_height)

	def close_search():
		global qua, open_search_btn, search_line, no_search, serach_on

		serach_on = False

		search_line.destroy()
		no_search.destroy()

		open_search_btn = Button(root, text=" search ", fg="#FFDE00", bg="#363636", cursor="hand2", command=lambda: search())
		open_search_btn.place(x=10, y=0+add_height)

		qua = Label(root, width=16, height=1, text="", font=((baseFont), "12"), bg=fg_titles, fg="#FFFF00", borderwidth=1, relief="ridge")
		qua.place(x=66, y=0+add_height)

		set_services()

	def search():
		global qua, open_search_btn, search_line, no_search, serach_on

		serach_on = True

		qua.destroy()
		open_search_btn.destroy()

		search_line = Entry(root, width=15, font=((baseFont), "13"), bg="#B5B5B5", fg="#242424")
		search_line.focus_set()
		search_line.bind('<KeyRelease>', lambda x: search_tag(search_line.get(), services_keys, all_service, END))
		search_line.place(x=10, y=0+add_height)

		no_search = Button(root, text=" close ", fg="#FFDE00", bg="#363636", cursor="hand2", command=lambda: close_search())
		no_search.place(x=171, y=0+add_height)

		search_tag(search_line.get(), services_keys, all_service, END)

	def past_del():
		text = root.clipboard_get()

		del_line.delete(0, END)
		del_line.insert(0, text)

	def past_detail():
		global mode, serach_on

		pos = all_service.index('insert')

		row = pos.split('.')[0]

		index = -1
		text = ''
		if (mode == 'view' and serach_on != True) or (mode == 'select_change' and serach_on != True):
			text = all_service.get(row+'.1', row+'.25')
		elif (mode == 'select_change' and serach_on == True) or (mode != 'select_change' and serach_on == True):
			text = all_service.get(row+'.0', row+'.25')
			if '>' in text:
				text = text.replace('> ', '')
		
		index = services_keys.index(text.lower())
		view_detail.delete(1.0, END)
		service_name.config(text='')
		view_detail.config(fg='#00FF00')
		view(index)

	def copy_name():
		global identify

		if identify:
			root.after_cancel(identify)

		text = service_name['text']

		if text != '':
			root.clipboard_clear()
			root.clipboard_append(text)

			console.config(text='Success copy "' + text + '"')

			identify = root.after(3000, console_clear)

	def copy_detail():
		global identify

		if identify:
			root.after_cancel(identify)

		pos = view_detail.index('insert')

		row = pos.split('.')[0]

		text = view_detail.get(row+'.0', row+'.25')

		if text != '':
			root.clipboard_clear()
			root.clipboard_append(text)

			if row == '1':
				console.config(text='Success copy "' + text + '"')
			elif row == '2':
				console.config(text='Success copy "' + text + '"')

			identify = root.after(3000, console_clear)

	def set_services():
		global services, services_keys, serach_on

		services_keys = []

		check = all_service.get(1.0, END)

		all_service.delete(1.0, END)
		all_service.config(fg=fg)
		all_service.tag_configure('center', justify='center')

		with open(dbPath) as f:
			services = json.load(f)

		if (len(services) != 0):
			for service in services:
				all_service.insert(END, " " + service["name"] + "\n", "center")
				services_keys.append(service["name"].lower())
		else:
			all_service.insert(END, "No services", "center")

		if check != '\n':
			all_service.see(END)

		if serach_on:
			search_tag(search_line.get(), services_keys, all_service, END)
		else:
			qua.config(text=str(len(services)) + ' services')

	def console_clear():
		console.config(text='', fg=fg)

	def name_in_services(name):
		return sum([service["name"] == name for service in services])

	def delete_from_services(name):
		global services
		services = [service for service in services if service["name"] != name]

	def auto_save():
		global name, login, password

		text = inf.get()

		if act_count == 1:
			name = text
		elif act_count == 2:
			login = text
		elif act_count == 3:
			password = text

	def del_s():
		global services, identify

		if identify:
			root.after_cancel(identify)

		name = del_line.get()

		if name_in_services(name):
			delete_from_services(name)

			if name == service_name['text']:
				service_name.config(text='')
				view_detail.delete(1.0, END)

			with open(dbPath, 'w') as f:
				json.dump(services, f, sort_keys=True, indent=4)

			del_line.delete(0, END)

			set_services()

			console.config(text='Success DELETE  "' + name + '"', fg='#00FF00')
		else:
			console.config(text='"' + name + '"  is not defined', fg='#FF0800')
		
		identify = root.after(3000, console_clear)

	def add():
		global name, login, password, name_to_change, identify

		if identify:
			root.after_cancel(identify)

		if what_to_dos == 'add':
			with open(dbPath, 'w') as f:
				service = {
					"name": name,
					"login": enc.encrypt(login, KEY, separator),
					"password": enc.encrypt(password, KEY, separator)
				}

				services.append(service)

				json.dump(services, f, sort_keys=True, indent=4)
		else:
			delete_from_services(name_to_change)

			with open(dbPath, 'w') as f:
				service = {
					"name": name,
					"login": enc.encrypt(login, KEY, separator),
					"password": enc.encrypt(password, KEY, separator)
				}

				services.append(service)

				json.dump(services, f, sort_keys=True, indent=4)

		if what_to_dos == 'add':
			console.config(text='Success ADD  "' + name + '"', fg='#00FF00')
			identify = root.after(3000, console_clear)
		else:
			console.config(text='Success CHANGE  "' + name_to_change + '"', fg='#00FF00')
			identify = root.after(3000, console_clear)

		set_services()

		if what_to_dos == 'add':
			back_to_start_add()
		else:
			back_to_start_change()

	def back_to_start_add():
		global do_add, do_change, name, login, password, next_btn, tablo, yes_btn, no_btn, what_to_dos, act_count
		global next_btn, back_btn, inf
			
		if act_count == 4:
			yes_btn.destroy()
			tablo.destroy()
			no_btn.destroy()
		else:
			next_btn.destroy()
			back_btn.destroy()
			inf.destroy()

		inf_name.config(fg='#FFFF04')

		mode = 'view'
		act_count = 1
		name = ''
		login = ''
		password = ''

		set_whattodo_btn()

	def back_to_start_change():
		global mode, cancel, filed_name, filed_login, filed_password, tablo, yes_btn, no_btn
		global name, login, password, act_count, name_to_change

		if act_count == 4:
			yes_btn.destroy()
			tablo.destroy()
			no_btn.destroy()
		else:
			cancel.destroy()

		mode = 'view'
		filed_name = ''
		inf_name.config(fg='#FFFF04')
		act_count = 1
		name = ''
		login = ''
		password = ''

		set_whattodo_btn()

	def back():
		global act_count, name, login, password, rnd_pass_btn

		if act_count == 1:
			back_to_start_add()
		elif act_count == 2:
			act_count -= 1
			inf_name.config(text='Name', fg='#FFFF00')
			inf.delete(0, END)
			inf.insert(0, name)
		elif act_count == 3:
			act_count -= 1
			inf_name.config(text='Login', fg='#FFFF00')
			rnd_pass_btn.destroy()
			inf.delete(0, END)
			inf.insert(0, login)

	def set_rnd_password(count):
		global inf, password, what_to_dos

		password = random_password(count)

		if what_to_dos == 'add':
			inf.delete(0, END)
			inf.insert(0, password)
		else:
			filed_password.delete(0, END)
			filed_password.insert(0, password)

	def next():
		global name, login, password, inf, next_btn, tablo, yes_btn, no_btn, services
		global act_count, filed_name, filed_login, filed_password, what_to_dos, rnd_pass_btn

		info = ''
		if what_to_dos == 'add':
			info = inf.get()

		if info != '' or what_to_dos == 'change':
			if act_count == 1:
				if name_in_services(info) == False:
					name = info
					inf_name.config(text='Login', fg='#FFFF00')
					act_count += 1
					inf.delete(0, END)
					inf.insert(0, login)
				else:
					inf_name.config(text='This name alredy defined', fg='#FF0800')
			elif act_count == 2:
				login = info

				inf_name.config(text="Password")

				inf.delete(0, END)
				inf.insert(0, password)

				rnd_pass_btn = Button(root, text="generate*", fg="#FFDE00", bg="#363636", cursor="hand2", command=lambda: set_rnd_password(20))
				rnd_pass_btn.place(x=10, y=170+add_height)

				act_count += 1	
			elif act_count == 3:

				if what_to_dos == 'add':
					password = info

					inf_name.config(text="Add?")
					inf.destroy()
					next_btn.destroy()
					back_btn.destroy()

				else:
					inf_name.config(text="Save changes?")
					filed_name.destroy()
					filed_login.destroy()
					filed_password.destroy()

				rnd_pass_btn.destroy()

				text = name + '\n' + login + '\n' + password

				tablo = Label(root, text=text, width=22, height=4, font=((baseFont), "12"), bg="#101010", fg=fg, borderwidth=1, relief="ridge")
				tablo.place(x=10, y=140+add_height)

				yes_btn = Button(root, text="yes", fg='#FFFF00', bg="#000000", cursor="hand2", command=lambda: add())
				yes_btn.place(x=80, y=222+add_height)

				if what_to_dos == 'add':
					no_btn = Button(root, text="no", fg='#FFFF00', bg="#000000", cursor="hand2", command=lambda: back_to_start_add())
					no_btn.place(x=114, y=222+add_height)
				else:
					no_btn = Button(root, text="no", fg='#FFFF00', bg="#000000", cursor="hand2", command=lambda: back_to_start_change())
					no_btn.place(x=114, y=222+add_height)

				act_count += 1		

	def view(index):
		global cancel, filed_name, filed_login, filed_password, end_change_btn, mode, serach_on

		if (mode == 'view' and serach_on == True) or (mode == 'view' and serach_on != True):
			view_detail.delete(1.0, END)
			service_name.config(text='')
			view_detail.tag_configure('center', justify='center')

			if index >= 0:
				name = services[index]["name"]
				if name_in_services(name):
					login = services[index]["login"]
					password = services[index]["password"]

					service_name.config(text=name)

					view_detail.insert(END, enc.decrypt(login, KEY, separator) + "\n", "center")
					view_detail.insert(END, enc.decrypt(password, KEY, separator), "center")

					view_detail.config(fg='#FFFF00')
					service_name.config(fg='#FFFF00')
				else:
					view_detail.insert(END, "Service not found", "center")
					service_name.config(text="Error")

					service_name.config(fg='#FF0800')
					view_detail.config(fg='#FF0800')
			else:
				view_detail.insert(END, "Enter service name..")
				view_detail.config(fg='#00FF00')
		elif (mode == 'select_change' and serach_on == True) or (mode == 'select_change' and serach_on != True):
			if index >= 0:
				name = services[index]["name"]
				if name_in_services(name):
					login = services[index]["login"]
					password = services[index]["password"]
					create_change_field(name, login, password)

	def set_add():
		global inf, next_btn, back_btn, what_to_dos

		what_to_dos = 'add'

		do_add.destroy()
		do_change.destroy()

		inf_name.config(text="Name")

		inf = Entry(root, width=22, font=((baseFont), "12"), bg='#818181', fg='#101010', justify='center')
		inf.bind("<Return>", lambda x: next())
		inf.bind('<KeyRelease>', lambda x: auto_save())
		inf.place(x=9, y=141+add_height)
		inf.focus_set()

		next_btn = Button(root, text=" next >>>", fg=fg, bg="#000000", cursor="hand2", command=lambda: next())
		next_btn.place(x=148, y=170+add_height)

		back_btn = Button(root, text="<<< back ", fg=fg, bg="#000000", cursor="hand2", command=lambda: back())
		back_btn.place(x=77, y=170+add_height)

	def end_change():
		global act_count, name, login, password, filed_name, filed_login, filed_password, cancel, end_change_btn

		act_count = 3

		name = filed_name.get()
		login = filed_login.get()
		password = filed_password.get()

		filed_name.destroy()
		filed_login.destroy()
		filed_password.destroy()
		cancel.destroy()
		end_change_btn.destroy()

		if name and login and password:
			next()

	def create_change_field(name, login, password):
		global filed_name, filed_login, filed_password, mode, cancel, end_change_btn, name_to_change, rnd_pass_btn

		mode = 'view'

		inf_name.config(text='Change "' + name + '"')

		cancel.destroy()

		name_to_change = name

		filed_name = Entry(root, width=22, font=((baseFont), "12"), bg='#818181', fg='#101010', justify='center')
		filed_name.bind("<Return>", lambda x: filed_login.focus_set())
		filed_name.place(x=9, y=141+add_height)
		filed_name.focus_set()
		filed_name.insert(0, name)

		filed_login = Entry(root, width=22, font=((baseFont), "12"), bg='#818181', fg='#101010', justify='center')
		filed_login.bind("<Return>", lambda x: filed_password.focus_set())
		filed_login.place(x=9, y=171+add_height)
		filed_login.insert(0, enc.decrypt(login, KEY, separator))

		filed_password = Entry(root, width=22, font=((baseFont), "12"), bg='#818181', fg='#101010', justify='center')
		filed_password.bind("<Return>", lambda x: end_change())
		filed_password.place(x=9, y=201+add_height)
		filed_password.insert(0, enc.decrypt(password, KEY, separator))

		rnd_pass_btn = Button(root, text="generate*", fg="#FFDE00", bg="#363636", cursor="hand2", command=lambda: set_rnd_password(20))
		rnd_pass_btn.place(x=10, y=230+add_height)

		cancel = Button(root, text="cancel", fg=fg, bg="#000000", cursor="hand2", command=lambda: set_change())
		cancel.place(x=100, y=230+add_height)

		end_change_btn = Button(root, text="next >>>", fg=fg, bg="#000000", cursor="hand2", command=lambda: end_change())
		end_change_btn.place(x=152, y=229+add_height)

	def set_change():
		global mode, inf_name, what_to_dos, cancel, filed_name, filed_login, filed_password, end_change_btn

		if filed_name:
			filed_name.destroy()
			filed_login.destroy()
			filed_password.destroy()
			cancel.destroy()
			end_change_btn.destroy()
			rnd_pass_btn.destroy()
		else:
			do_add.destroy()
			do_change.destroy()

		what_to_dos = 'change'
		mode = 'select_change'

		inf_name.config(text='Select service.. ↑')

		cancel = Button(root, text="cancel", fg=fg, bg="#000000", cursor="hand2", command=lambda: back_to_start_change())
		cancel.place(x=90, y=145+add_height)

	def set_whattodo_btn():
		global do_add, do_change

		inf_name.config(text="What to do?")

		do_add = Button(root, text="add+", fg=fg, bg="#000000", cursor="hand2", command=lambda: set_add())
		do_add.place(x=66, y=145+add_height)

		do_change = Button(root, text="change+", fg=fg, bg="#000000", cursor="hand2", command=lambda: set_change())
		do_change.place(x=112, y=145+add_height)

	set_services()
	set_whattodo_btn()

def enterKeyCode():
	def validate(value):
		if (value.isdigit() or value == "") and len(value) < 20:
			return True
		return False

	keyCodeLabel = Label(root, text="Key code: ", font=((baseFont), "14"), bg='#000000', fg=fg)
	keyCodeEntry = Entry(root, font=((baseFont), "14"), bg=fg_titles, fg=fg, justify='center', validate="key")
	keyCodeEntry["validatecommand"] = (keyCodeEntry.register(validate), '%P')

	def setKey(key):
		global KEY
		if key:
			KEY = int(key)
			keyCodeEntry.destroy()
			keyCodeLabel.destroy()
			main()

	keyCodeEntry.bind("<Return>", lambda _: setKey(keyCodeEntry.get()))
	keyCodeEntry.focus_set()
	keyCodeLabel.place(relx=0.5, rely=0.44, anchor=CENTER)
	keyCodeEntry.place(relx=0.5, rely=0.5, anchor=CENTER)

if __name__ == '__main__':
	enterKeyCode()

	root.bind("<Escape>", lambda _: exit())
	root.resizable(0, 0)
	root.mainloop()