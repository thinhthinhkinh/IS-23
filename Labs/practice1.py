#Bai 1
def ktsnt(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5) +1):
        if n % i == 0:
            return False
    return True
    #cach 1
def insnt(n):
    for n in range(1, n+1):
        if ktsnt(n):
            print(n)
    #cach 2
n = int(input("Nhap so nguyen n: "))
print("Cac so nguyen to tu 1 den", n, "la: ")
for i in range( n+1):
    if ktsnt(i):
        print(i)

# #Bai 2
def sum_of_digits(n):
  if not 100 <= n <= 999:
    return "Số không hợp lệ. Vui lòng nhập số nguyên có 3 chữ số."

  total = 0
  while n > 0:
    digit = n % 10
    total += digit
    n //= 10
  return total

n = int(input("Nhập vào số nguyên n có 3 chữ số: "))
result = sum_of_digits(n)
print("Tổng các chữ số của", n, "là:", result)

#Bai 3
nhap_chuoi = input("Nhap vao mot day cac so nguyen cach nhau boi khoang trang")
mang = []
for i in nhap_chuoi.split():
    mang.append(int(i))
print("Mang da nhap: ", mang)

tong = 0
for n in mang:
    tong += n
print("Tong cac phan tu trong mang: ", tong)

max_num = mang[0]
for n in mang:
    if n > max_num:
        max_num = n
print("So lon nhat trong mang: ", max_num)

min_num = mang[0]
for n in mang:
    if n < min_num:
        min_num = n
print("So nho nhat trong mang: ", min_num)

sapxep = []
while array:
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_num = num
    sapxep.append(max_num)
    array.remove(max_num)
print("Mảng sau khi sắp xếp theo thứ tự giảm dần:", sapxep)


sochan = []
for num in array:
    if num % 2 == 0:
        sochan.append(num)
print("Các số chẵn trong mảng:", sochan)

#Bai 5
n = int(input("Nhập vào một số nguyên dương: "))

if n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
  chuyendoi = str(n)
  if chuyendoi == chuyendoi[::-1]:
    print(n, "là số đối xứng.")
  else:
    print(n, "không phải là số đối xứng.")

#Bai 9
def songuyen(nhap):
  songuyen = list(set(nhap))
  return songuyen
so = [1,2,3,4,5,6,6,7,8,8,9,9,2,3,9]
kqua = songuyen(so)
print("Danh sach cac so khong trung nhau: ",kqua)

#Bai10
def mahoa(L):

    D = {}
    for item in L:
        if item not in D:
            D[item] = len(D)

    L_mahoa = [D[item] for item in L]

    return D, L_mahoa

L = ["đen", "vàng", "xanh", "vàng", "xanh", "đỏ", "hồng"]
D = {'đen':0,'vàng':1,'xanh':2,'đỏ':3,'hồng':4}
print("Danh sách đã mã hóa:", L_mahoa)


