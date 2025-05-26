def filter_gioi(scores):
    """
    Trả về danh sách điểm giỏi (>=8) trong khoảng hợp lệ [0, 10].
    Nếu scores là None hoặc rỗng thì trả về danh sách rỗng.
    """
    if not scores:
        return []
    return [score for score in scores if 8 <= score <= 10]


def average_score(scores):
    """
    Tính trung bình cộng các điểm hợp lệ (0 <= score <= 10).
    Nếu scores là None, rỗng hoặc không có điểm hợp lệ thì trả về 0.
    """
    if not scores:
        return 0
    valid_scores = [score for score in scores if 0 <= score <= 10]
    return sum(valid_scores) / len(valid_scores) if valid_scores else 0


# Nếu bạn muốn test trực tiếp file này, bỏ comment phần sau:
# if __name__ == "__main__":
#     test_scores = [9, 7.5, -1, 10, 8.2, 11, None]
#     print("Danh sách điểm:", test_scores)
#     print("Học sinh giỏi:", filter_gioi(test_scores))
#     print("Điểm trung bình:", average_score(test_scores))
