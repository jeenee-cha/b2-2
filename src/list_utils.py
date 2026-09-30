"""목록 처리에 사용하는 유틸리티 함수."""


def unique_preserve_order(values):
    """중복을 제거하고 값이 처음 등장한 순서를 유지한다.

    Example:
        >>> unique_preserve_order([3, 1, 3, 2, 1])
        [3, 1, 2]
    """
    unique_values = []

    for value in values:
        if value not in unique_values:
            unique_values.append(value)

    return unique_values
