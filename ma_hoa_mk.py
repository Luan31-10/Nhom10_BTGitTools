import hashlib

print("--- CHƯƠNG TRÌNH MÃ HÓA MẬT KHẨU ---")

# Nhập mật khẩu từ người dùng
mat_khau = input("Vui lòng nhập mật khẩu cần bảo mật: ")

# Tiến hành băm (hash) mật khẩu bằng thuật toán SHA-256
mat_khau_ma_hoa = hashlib.sha256(mat_khau.encode()).hexdigest()

# In kết quả
print(f"=> Mật khẩu gốc: {mat_khau}")
print(f"=> Mật khẩu đã mã hóa (SHA-256): {mat_khau_ma_hoa}")