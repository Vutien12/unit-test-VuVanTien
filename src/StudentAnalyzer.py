def filter_gioi(scores):
    """
    Trả về danh sách điểm >= 8 và trong khoảng hợp lệ [0, 10]
    """
    return [score for score in scores if 8 <= score <= 10]


def average_score(scores):
    """
    Tính trung bình cộng các điểm hợp lệ (0 <= score <= 10).
    Nếu danh sách trống hoặc không có điểm hợp lệ thì trả về 0.
    """
    valid_scores = [score for score in scores if 0 <= score <= 10]
    return sum(valid_scores) / len(valid_scores) if valid_scores else 0

# # 🔽 Thêm đoạn này để test trực tiếp
# if __name__ == "__main__":
#     test_scores = [9, 7.5, -1, 10, 8.2, 11]
#     print("Danh sách điểm:", test_scores)
#     print("Học sinh giỏi:", filter_gioi(test_scores))
#     print("Điểm trung bình:", average_score(test_scores))

