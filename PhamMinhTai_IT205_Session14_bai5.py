student_records = [
    {
        "student_id": "RA01",
        "name": "Nguyễn Văn Code",
        "current_points": 1500,
        "spent_points": 500,
        "refunded_points": 0,
        "multiplier": 1.0
    },
    {
        "student_id": "RA02",
        "name": "Trần Thị Bug",
        "current_points": 800,
        "spent_points": 1200,
        "refunded_points": 100,
        "multiplier": 1.5
    },
    {
        "student_id": "RA03",
        "name": "Lê Văn Fix",
        "current_points": 300,
        "spent_points": 0,
        "refunded_points": 0,
        "multiplier": 2.0
    }
]


def find_student(records, student_id):
    student_id = student_id.strip().upper()
    for i, s in enumerate(records):
        if s["student_id"] == student_id:
            return i
    return -1


def display_statements(records):
    if not records:
        print("Hệ thống chưa có dữ liệu.")
        return

    for i, s in enumerate(records, 1):
        p = s["current_points"]
        status = "Cần tích lũy thêm" if p < 500 else ("Thành viên tiềm năng" if p <= 1500 else "Thành viên ưu tú")

        print(
            f"{i}. {s['student_id']} | {s['name']} | "
            f"{p} | {s['spent_points']} | {s['refunded_points']} | x{s['multiplier']} | {status}"
        )


def redeem_rewards(records):
    idx = find_student(records, input("Mã: "))
    if idx == -1:
        print("Không tìm thấy!")
        return

    points = int(input("Điểm tiêu: "))
    if points <= 0:
        print("Điểm không hợp lệ")
        return

    if points > records[idx]["current_points"]:
        print("Không đủ điểm")
        return

    records[idx]["current_points"] -= points
    records[idx]["spent_points"] += points
    print("Giao dịch thành công")


def appeal_score(records):
    idx = find_student(records, input("Mã: "))
    if idx == -1:
        print("Không tìm thấy!")
        return

    points = int(input("Điểm hoàn: "))
    if points <= 0 or points > records[idx]["spent_points"]:
        print("Không hợp lệ")
        return

    records[idx]["spent_points"] -= points
    records[idx]["current_points"] += points
    records[idx]["refunded_points"] += points
    print("Hoàn điểm thành công")


def activate_multiplier(records):
    idx = find_student(records, input("Mã: "))
    if idx == -1:
        print("Không tìm thấy!")
        return

    try:
        m = float(input("Hệ số (1.0-3.0): "))
    except:
        print("Sai định dạng")
        return

    if m < 1.0 or m > 3.0:
        print("Hệ số không hợp lệ")
        return

    records[idx]["multiplier"] = m
    print("Kích hoạt thành công")


def grade_assignment(records):
    idx = find_student(records, input("Mã: "))
    if idx == -1:
        print("Không tìm thấy!")
        return

    base = int(input("Điểm gốc: "))
    if base <= 0:
        print("Không hợp lệ")
        return

    real = base * records[idx]["multiplier"]
    records[idx]["current_points"] += real

    print(f"Điểm thực nhận: {real}")


def menu():
    print("\n1. Sao kê")
    print("2. Đổi điểm")
    print("3. Hoàn điểm")
    print("4. Hệ số")
    print("5. Chấm bài")
    print("6. Thoát")


def main():
    while True:
        menu()
        c = input("Chọn: ")

        if c == "1":
            display_statements(student_records)
        elif c == "2":
            redeem_rewards(student_records)
        elif c == "3":
            appeal_score(student_records)
        elif c == "4":
            activate_multiplier(student_records)
        elif c == "5":
            grade_assignment(student_records)
        elif c == "6":
            print("Bye")
            break
        else:
            print("Sai lựa chọn")


if __name__ == "__main__":
    main()