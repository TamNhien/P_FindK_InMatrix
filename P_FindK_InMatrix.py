def find_element(matrix, k):
    # Duyệt qua từng hàng và cột của ma trận
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            # Nếu phần tử tại vị trí (i, j) bằng k, trả về vị trí đó
            if val == k:
                return i, j
    # Nếu không tìm thấy, trả về None
    return None

def main():
    # Nhập số hàng và số cột của ma trận
    n, m = map(int, input("Nhập số hàng và số cột của ma trận : ").split())

    # Nhập ma trận từ người dùng
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # Nhập số cần tìm
    k = int(input("Nhập số cần tìm : "))

    # Tìm vị trí của số trong ma trận
    result = find_element(matrix, k)

    # In kết quả
    if result:
        print(f"Vị trí của {k} trong ma trận là ({result[0]}, {result[1]})")
    else:
        print(f"{k} không có trong ma trận.")

if __name__ == "__main__":
    main()

