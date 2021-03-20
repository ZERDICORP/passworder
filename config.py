from tkinter import *
import win32api, random
import json
from win32api import GetSystemMetrics

VERSION = "0.4"

win32api.LoadKeyboardLayout("00000409", 1)

win_w = 434
win_h = 500

w_center_x = int((GetSystemMetrics(0)/2) - (win_w/2))
w_center_y = int((GetSystemMetrics(1)/2) - (win_h/2))

dbPath = "db/db.json"

baseFont = "Roboto"

# данные для шифрования паролей
KEY = 156
separator = {
	"dot": "[",
	"int_code": "]",
	"global_sep": "|"
}

# список всех сервисов
services = {}
services_keys = []
serv_list = []

# данные для добавления и изменения сервисов
name_to_change = ''
name = ''
login = ''
password = ''

what_to_dos = ''
mode = 'view'
serach_on = False

inf = ''
act_count = 1
next_btn = ''
back_btn = ''
do_add = ''
do_change = ''
tablo = ''
yes_btn = ''
no_btn = ''
identify = ''
cancel = ''
filed_name = ''
filed_login = ''
filed_password = ''
end_change_btn = ''
rnd_pass_btn = ''
search_line = ''
no_search = ''
qua = None
open_search_btn = None
inf_name = ""

fg = "#00FF00"
fg_titles = '#101010'
add_height = 75

color = ['#00FF00', '#00DE00', '#00A800']

line_x_1 = 0
line_x_2 = 600