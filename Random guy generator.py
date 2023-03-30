import os
import unidecode
import random as r
import subprocess
import pyperclip
import datetime
import string

def getRandomFrom(listname):
	return listname[r.randint(0,len(listname)-1)]

def copyToClipboard(txt):
    cmd='echo '+txt.strip()+'|pbcopy'
    return subprocess.check_call(cmd, shell=True)

os.system('cls')

def generate():
	ho = ['Nguyễn', 'Trần', 'Đặng', 'Phạm', 'Đậu', 'Ngô', 'Trịnh', 'Lý', 'Đoàn', 'Thái', 'Triệu']

	dem = ['Văn', 'Thị', 'Lâm', 'Đông', 'Gia', 'Quốc', 'Anh', 'Huy', 'Minh', 'Quang', 'Tố', 'Hải', 'Khải', 'Khánh', 'Ngọc', 'Sỹ','Thùy']

	ten = ['Thùy','Khoa', 'Mạnh', 'Nam', 'Bắc', 'Hoàng', 'Minh', 'Hoài', 'Lộc', 'Quang', 'Diệu', 'Liệu', 'Hải', 'Thi', 'Anh', 'Kha', 'Vinh', 'Dương', 'Ngọc', 'Quyền']

	road = ['Hàm Nghi', 'Nguyễn Bỉnh Khiêm', 'Pasteur', 'Trương Hán Siêu', 'Hàn Thuyên', 'Nguyễn Cảnh Chân', 'Phạm Hồng Thái', 'Võ Thị Sáu', 'Hồ Hảo Hớn', 'Nguyễn Công Chứ', 'Phạm Ngọc Thạch', 'Võ Văn Kiệt', 'Hồ Huấn Nghiệp', 'Nguyễn Cư Trinh', 'Phạm Ngũ Lão', 'Vỗ Văn Tần', 'Hồ Tùng Mậu', 'Nguyễn Cửu Vân', 'Phạm Viết Chánh', 'Yersin', 'Hòa Mỹ', 'Nguyễn Đình Chiểu', 'Phan Bội Châu', 'Hoàng Sa', 'Nguyễn Du', 'Phan Chu Chinh', 'Trần Bình Trọng', 'Trương Đăng Quế']

	password_symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{};:'\"\\|,.<>/?`~"

	letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', '']

	numbers = ['1','2','3','4','5','6','7','8','9','0']

	new_ho = getRandomFrom(ho)
	new_dem = getRandomFrom(dem)
	new_ten = getRandomFrom(ten)

	#get name here 
	fullname = str(new_ho+" "+new_dem+" "+new_ten)

	#email domains
	domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'googlemail.com', 'icloud.com', 'proton.me', 'juno.com', 'cheovani.ru', 'onedrive.com', 'outlook.uk', 'outlook.de', 'sublime.com', 'ggweb.com']

	#username
	username = str(unidecode.unidecode(fullname).replace(' ','').lower()+str(r.randint(99,9876)))

	#generated email
	mail = str(unidecode.unidecode(fullname).replace(' ','').lower()+str(r.randint(99,9876))+"@"+getRandomFrom(domains))

	#random ip
	ip = str(str(r.randint(1,99))+"."+str(r.randint(1,999))+"."+str(r.randint(1,10))+"."+str(r.randint(1,999)))
	
	#random address
	address = str(str(r.randint(0,999))+getRandomFrom(letters)+" "+str(getRandomFrom(road)))
	
	#password
	password = ""
	for i in range(10):
		password = password + getRandomFrom(password_symbols)

	#id number
	id_number = ""
	for i in range(13):
		id_number = id_number + getRandomFrom(numbers)

	today = datetime.date.today()
	oldest_date = today - datetime.timedelta(days=365*40)
	sinhnhat = oldest_date + datetime.timedelta(days=r.randint(0, (today - oldest_date).days))

	return str("  Họ và Tên: "+fullname+"\n Username: "+username+"\n Email: "+mail+"\n IP: "+ip+"\n Địa chỉ: "+address+"\n CCCD/CMND: "+id_number+"\n Password: "+password+"\n DOB: "+str(sinhnhat.strftime('%d/%m/%Y')))



bruh = generate()
pyperclip.copy(bruh)
print(bruh)
print("\n >>> Copied to clipboard!")