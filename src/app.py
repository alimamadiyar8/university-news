"""Университет жаңалықтары қосымшасы."""

news_list = [
    {"id": 1, "title": "Жаңа оқу жылы басталды", "body": "2025-2026 оқу жылы басталды."},
    {"id": 2, "title": "Халықаралық конференция", "body": "Университетте конференция өтті."},
]


def get_all_news():
    """Барлық жаңалықтарды қайтарады."""
    return news_list


def get_news_by_id(news_id):
    """ID бойынша жаңалықты қайтарады."""
    for news in news_list:
        if news["id"] == news_id:
            return news
    return None


def add_news(title, body):
    """Жаңа жаңалық қосады."""
    new_id = max([n["id"] for n in news_list], default=0) + 1
    new_news = {"id": new_id, "title": title, "body": body}
    news_list.append(new_news)
    return new_news


def count_news():
    """Жаңалықтар санын қайтарады."""
    return len(news_list)


if __name__ == "__main__":
    print(f"Барлық жаңалықтар саны: {count_news()}")
    for n in get_all_news():
        print(f"- {n['title']}")