def filter_gioi(scores):
    """
    Trả về danh sách điểm >= 8 và trong khoảng hợp lệ [0, 10]
    """
    if not scores:
        return []

    gioi = []
    for score in scores:
        if 0 <= score <= 10 and score >= 8:
            gioi.append(score)
    return gioi


def average_score(scores):
    """
    Tính trung bình cộng các điểm hợp lệ (0 <= score <= 10).
    Nếu danh sách trống hoặc không có điểm hợp lệ thì trả về 0.
    """
    if not scores:
        return 0

    total = 0
    count = 0
    for score in scores:
        if 0 <= score <= 10:
            total += score
            count += 1

    return total / count if count > 0 else 0




# # 🔽 Thêm đoạn này để test trực tiếp
# if __name__ == "__main__":
#     test_scores = [9, 7.5, -1, 10, 8.2, 11]
#     print("Danh sách điểm:", test_scores)
#     print("Học sinh giỏi:", filter_gioi(test_scores))
#     print("Điểm trung bình:", average_score(test_scores))

