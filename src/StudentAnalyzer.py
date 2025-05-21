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
