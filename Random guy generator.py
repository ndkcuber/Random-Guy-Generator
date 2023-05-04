import os, datetime
import random as r
from platform import system
try:
    import pyperclip
    from unidecode import unidecode
except:
    os.system('pip install pyperclip unidecode')
    import pyperclip
    from unidecode import unidecode

def getRandomFrom(listname):
	return listname[r.randint(0,len(listname)-1)]

if system()=="Linux":os.system('clear')
else: os.system("cls")

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
	username = unidecode(fullname).replace(' ','').lower()+str(r.randint(99,9876))

	#generated email
	mail = unidecode(fullname).replace(' ','').lower()+str(r.randint(99,9876))+"@"+getRandomFrom(domains)

	#random ip
	ip = "{}.{}.{}.{}".format(*[r.randint(0,99) for i in range(4)])
	
	#random address
	address = str(r.randint(0,999))+getRandomFrom(letters)+" "+getRandomFrom(road)
	
	#password
	password = "".join([getRandomFrom(password_symbols) for i in range(10)])

	#id number
	id_number = "".join([getRandomFrom(numbers) for i in range(10)])

	today = datetime.date.today()
	oldest_date = today - datetime.timedelta(days=365*40)
	sinhnhat = oldest_date + datetime.timedelta(days=r.randint(0, (today - oldest_date).days))

	return str("  Họ và Tên: "+fullname+"\n Username: "+username+"\n Email: "+mail+"\n IP: "+ip+"\n Địa chỉ: "+address+"\n CCCD/CMND: "+id_number+"\n Password: "+password+"\n DOB: "+str(sinhnhat.strftime('%d/%m/%Y')))

bruh = generate()
pyperclip.copy(bruh)
print(bruh)
print("\n >>> Copied to clipboard!")
