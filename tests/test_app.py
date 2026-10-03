"""Университет жаңалықтары қосымшасының тестілері."""
from src.app import (
    get_all_news,
    get_news_by_id,
    add_news,
    count_news,
)


def test_get_all_news_returns_list():
    """1-тест: жаңалықтар тізімі қайтарылуы керек."""
    result = get_all_news()
    assert isinstance(result, list)
    assert len(result) >= 2


def test_get_news_by_id_returns_correct_news():
    """2-тест: ID бойынша дұрыс жаңалық қайтарылуы керек."""
    news = get_news_by_id(1)
    assert news is not None
    assert news["id"] == 1
    assert "title" in news


def test_add_news_increases_count():
    """3-тест: жаңа жаңалық қосқанда саны артуы керек."""
    initial = count_news()
    add_news("Тестілік жаңалық", "Тестілік сипаттама")
    assert count_news() == initial + 1


def test_get_news_by_id_returns_none_for_unknown_id():
    """4-тест: белгісіз ID үшін None қайтарылуы керек."""
    assert get_news_by_id(9999) is None