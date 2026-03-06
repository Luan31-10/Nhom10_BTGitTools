students = []

while True:
    print("\n--- QUẢN LÝ SINH VIÊN ---")
    print("1. Thêm sinh viên")
    print("2. Xem danh sách sinh viên")
    print("3. Tìm sinh viên")
    print("4. Thoát")

    choice = input("Chọn chức năng: ")

    if choice == "1":
        name = input("Nhập tên sinh viên: ")
        students.append(name)
        print("Đã thêm sinh viên.")

    elif choice == "2":
        print("Danh sách sinh viên:")
        for s in students:
            print("-", s)

    elif choice == "3":
        search = input("Nhập tên cần tìm: ")
        if search in students:
            print("Tìm thấy sinh viên:", search)
        else:
            print("Không tìm thấy.")

    elif choice == "4":
        print("Thoát chương trình.")
        break

    else:
        print("Lựa chọn không hợp lệ.")
