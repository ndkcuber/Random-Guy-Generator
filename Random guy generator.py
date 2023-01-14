import os
import unidecode
import random as r

os.system('cls')

def generate():
	ho = ['Nguyễn', 'Trần', 'Đặng', 'Phạm', 'Đậu', 'Ngô', 'Trịnh', 'Lý', 'Đoàn', 'Thái', 'Triệu']

	dem = ['Văn', 'Thị', 'Lâm', 'Đông', 'Gia', 'Quốc', 'Anh', 'Huy', 'Minh', 'Quang', 'Tố', 'Hải', 'Khải', 'Khánh', 'Ngọc', 'Sỹ']

	ten = ['Khoa', 'Mạnh', 'Nam', 'Bắc', 'Hoàng', 'Minh', 'Hoài', 'Lộc', 'Quang', 'Diệu', 'Liệu', 'Hải', 'Thi', 'Anh', 'Kha', 'Vinh', 'Dương', 'Ngọc', 'Quyền']

	new_ho = ho[r.randint(0,len(ho)-1)]
	new_dem = dem[r.randint(0,len(dem)-1)]
	new_ten = ten[r.randint(0,len(ten)-1)]

	#get name here 
	fullname = str(new_ho+" "+new_dem+" "+new_ten)

	#email domains
	domains = ['gmail.com', 'hotmail.com', 'yahoo.com', 'outlook.com', 'googlemail.com', 'icloud.com', 'proton.me', 'juno.com'] 

	#username
	username = str(unidecode.unidecode(fullname).replace(' ','').lower()+str(r.randint(99,1840)))

	#generated email
	mail = str(unidecode.unidecode(fullname).replace(' ','').lower()+str(r.randint(99,1840))+"@"+domains[r.randint(0,len(domains)-1)])

	ip = str(str(r.randint(1,99))+"."+str(r.randint(1,999))+"."+str(r.randint(1,10))+"."+str(r.randint(1,999)))

	print("Họ và Tên: "+fullname)
	print("Email: "+mail)
	print("Username: "+username)
	print("IP: "+ip)

generate()