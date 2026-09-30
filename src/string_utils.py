"""문자열 처리에 사용하는 유틸리티 함수."""


def normalize_whitespace(text):
    """연속된 공백·줄바꿈·탭을 한 칸으로 줄이고 앞뒤 공백을 제거한다.

    Example:
        >>> normalize_whitespace("  hello\\n team\\tgit  ")
        'hello team git'
    """
    return " ".join(text.split())
