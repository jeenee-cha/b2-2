"""숫자 처리에 사용하는 유틸리티 함수."""


def clamp(value, minimum, maximum):
    """값을 minimum 이상 maximum 이하 범위로 제한한다.

    minimum이 maximum보다 크면 ValueError를 발생시킨다.

    Example:
        >>> clamp(15, 0, 10)
        10
    """
    if minimum > maximum:
        raise ValueError("minimum은 maximum보다 클 수 없습니다.")

    if value < minimum:
        return minimum

    if value > maximum:
        return maximum

    return value
