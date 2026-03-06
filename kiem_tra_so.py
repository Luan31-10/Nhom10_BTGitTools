print("--- CHƯƠNG TRÌNH KIỂM TRA SỐ CHẴN LẺ ---")

# Nhập số nguyên từ người dùng
so_nhap_vao = int(input("Vui lòng nhập vào một số nguyên: "))

# Kiểm tra chẵn lẻ và in ra kết quả
if so_nhap_vao % 2 == 0:
    print(f"=> Số {so_nhap_vao} là SỐ CHẴN.")
else:
    print(f"=> Số {so_nhap_vao} là SỐ LẺ.")
