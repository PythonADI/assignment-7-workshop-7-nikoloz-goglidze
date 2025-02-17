import re


def test_word_count() -> None:
    try:
        from src.assignment.main import get_word_count
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "Please create python file with name of `main.py` in `src/assignments/` directory"
        ) from e
    except ImportError as e:
        raise ImportError("Please create functions as described in README") from e

    assert get_word_count("Hello There") == 2
    assert get_word_count("Hello   ") == 1
    assert get_word_count("Hello   There") == 2
    assert get_word_count("  Hello   There  ") == 2
    assert get_word_count("This is a really long message " * 10) == 60
    assert get_word_count("This is a really long message        " * 10) == 60
    assert get_word_count("This is          a really long message        " * 10) == 60
    assert (
        get_word_count("      This is          a really long message        " * 10) == 60
    )
    assert (
        get_word_count("      This    is          a really long message        " * 10) == 60
    )


def test_price() -> None:
    try:
        from src.assignment.main import get_price
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "Please create python file with name of `main.py` in `src/assignments/` directory"
        ) from e
    except ImportError as e:
        raise ImportError("Please create functions as described in README") from e

    assert get_price("Hello There") == 0.02
    assert get_price("Hello There  ") == 0.02
    assert get_price("  Hello There  ") == 0.02
    assert get_price("  Hello   There  ") == 0.02
    assert get_price("This is a really long message " * 10) == 0.6
    assert get_price("  This is a really long message " * 10) == 0.6
    assert get_price("  This is a really   long message " * 10) == 0.6
    assert get_price("  This is a really   long message " * 100) == 6.0


def test_get_total_price() -> None:
    try:
        from src.assignment.main import get_total_price
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "Please create python file with name of `main.py` in `src/assignments/` directory"
        ) from e
    except ImportError as e:
        raise ImportError("Please create functions as described in README") from e

    messages = [f"Message {i}" for i in range(100)]
    assert get_total_price(messages) == 2
    messages.append("This is a Rally long message " * 100)
    assert get_total_price(messages) == 8
    messages.append("       This is a Rally long message " * 100)
    assert get_total_price(messages) == 14

    assert get_total_price([]) == 0


def test_format_message() -> None:
    try:
        from src.assignment.main import format_message
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "Please create python file with name of `main.py` in `src/assignments/` directory"
        ) from e
    except ImportError as e:
        raise ImportError("Please create functions as described in README") from e

    assert re.match("From: Test+\nMessage: .+", format_message("Test", "Hello there"))
    assert re.match(
        "From: George+\nMessage: .+",
        format_message("George", "This is what it is " * 100),
    )
    assert format_message("", "Mesage") == "Invalid Message"
    assert format_message("Test", "") == "Invalid Message"


def test_format_messages() -> None:
    try:
        from src.assignment.main import format_messages
    except ModuleNotFoundError as e:
        raise ModuleNotFoundError(
            "Please create python file with name of `main.py` in `src/assignments/` directory"
        ) from e
    except ImportError as e:
        raise ImportError("Please create functions as described in README") from e

    messages = [f"Message {i} " * i for i in range(1, 100)]

    for formatted_message in format_messages("Test", messages):
        assert re.match(
            r"From: Test\nMessage: .+", formatted_message
        ), "Please check the format of the message"
    for formatted_message in format_messages("", messages):
        assert (
            formatted_message == "Invalid Message"
        ), "Please check the format of the message"
