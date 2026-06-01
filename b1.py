""" 
        HỆ THỐNG QUẢN LÝ GIỎ HÀNG AMAZON
INPUT:  Dữ liệu đề bài cho
    + cho dữ liệu giỏ hàng : list []
    [
        {},
        {},
        {}
    ]
    + từng sản phẩm sẽ có các thuộc tính
        + id sản phẩm
        + tên sản phẩm
        + số lượng sản phẩm
        + đơn giá 1 sản phẩm
OUTPUT: kết quả
    1. Xem chi tiết giỏ hàng
        + Xem thông tin từng sản phẩm trong giỏ hàng
    2. Thêm sản phẩm vào giỏ hàng
        + Nhập mã sản phẩm:
            TH1: mã sản phẩm đã tồn tại: thì nhập số lượng để cộng dồn
             ( kiểm tra người không đúng số, số âm)
            TH2: mã sản phẩm không tồn tại: 
                cho nhập tên, số lượng, giá, (kiểm tra số lượng, giá : thỏa mãn
                điều kiện không âm...)
    3. Cập nhật số lượng sản phẩm
        -Nhập mã sản phẩm cần cập nhật
            + Nếu đã tồn tại thì nhập số lượng mới: kiểm tra dữ liệu rồi cập nhật
            + Nếu không tồn tại thì thông báo
    4. Xóa sản phẩm trong giỏ hàng
        - Nhập mã sản phẩm cần xóa
            + Kiểm tra mã sản phẩm có tồn tại hay không
                TH1: Nếu có thì xóa: theo index hoặc giá trị
                TH2: Nếu không có thì thông báo mã sản phẩm không tồn tại
    5. Thoát chương trình
"""

art_items = [
         {
         	"id": "P001", 
         	"name": "Dien thoai iPhone 15",
         	"number": 1,
         	"price": 25000000
         },
         {
         	"id": "P002",
         	"name": "Op lung Silicon", 
         	"number": 2, 
         	"price": 150000
         }
]

while True:
    print("""
=====================================================
            SHOPEE CART MANAGEMENT SYSTEM
=====================================================
1. Xem chi tiết giỏ hàng & Tính tổng tiền
2. Thêm sản phẩm mới / Cộng dồn số lượng
3. Cập nhật số lượng của một sản phẩm
4. Xóa sản phẩm khỏi giỏ hàng
5. Thoát chương trình
=====================================================""")
    choice = input("Mời bạn chọn chức năng (1-5): ")
    print()
    match choice:
        case "1":
            count_number = 0
            sum_price = 0
            total_price = 0
            count_quantity = 0
            print("--- CHI TIẾT GIỎ HÀNG ---")
            print(f"{'STT':<5}| {'Mã SP':<10}| {'Tên sản phẩm:':<30}| {'SL':<5}| {'Đơn giá':<20}| {'Thành tiền':<20}")
            print("-" * 95)

            for emp in art_items:
                count_number += 1
                id = emp["id"]
                name = emp["name"]
                number = emp["number"] 
                price = emp["price"]

                sum_price = price * number

                total_price += sum_price

                count_quantity += number

                print(f"{count_number:<5}| {id:<10}| {name:<30}| {number:<5}| {price:<20}| {sum_price:<20,}")

            print("-" * 95)
            print()
            print(f"=> Tổng số lượng sản phẩm trong giỏ: {count_quantity}")
            print(f"=> TỔNG TIỀN THANH TOÁN: {total_price:,}")

        case "2":
            product_add = {}
            flag = 0
            input_id = input("Nhập mã sản phẩm cần thêm: ").strip().upper()
            for emp in art_items:
                if input_id == emp["id"]:
                    flag = 1
                    emp["number"] += 1  
                    print("Thêm số lượng thành công")
                    break               
            if flag == 0:
                input_name = input("Nhập tên sản phẩm: ").strip().title()

                input_quantity = int(input("Nhập số lượng sản phẩm: "))
                while input_quantity < 0:
                    print("Số lượng phải lớn hơn 0")
                    input_quantity = int(input("Nhập số lượng sản phẩm: "))

                input_price = float(input("Nhập đơn giá sản phẩm: "))
                while input_price < 0:
                    print("Giá không được là số âm")
                    input_price = float(input("Nhập đơn giá sản phẩm: "))
                
                product_add["id"] = input_id
                product_add["name"] = input_name
                product_add["number"] = input_quantity
                product_add["price"] = input_price

                art_items.append(product_add)    

        case "3":
            flag = 0
            input_id = input("Nhập mã sản phẩm: ").strip().upper()
            for emp in art_items:
                if input_id == emp["id"]:
                    flag = 1
                    number = int(input("Nhập số lượng mới cần thay đổi: "))
                    while number < 0:
                        print("Số lượng không hợp lệ")
                        number = int(input("Nhập số lượng mới cần thay đổi: "))
                    emp["number"] = number
                    print("Cập nhật thành công")
            if flag == 0:
                print("Mã sản phẩm không tồn tại")

        case "4":
            flag = 0
            i = -1
            input_delete_id = input("Nhập mã sản phẩm muốn xóa: ").strip().upper()
            for emp in art_items:
                i += 1
                if input_delete_id == emp["id"]:
                    flag = 1
                    art_items.pop(i)
                    print("Đã xóa thành công")
            if flag == 0:
                print("Không tìm thấy mã sản phẩm để xóa")

        case "5":
            print("Đã thoát chương trình!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại!")