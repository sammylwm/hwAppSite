import re
import requests

def convert_rub_to_eur_in_text(text: str) -> str:
    # 1. Получаем курс евро
    url = "https://www.fontanka.ru/currency.html"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    resp.raise_for_status()
    html = resp.text

    match = re.search(
        r"<td[^>]*>eur</td>\s*<td[^>]*>[^<]*</td>\s*<td[^>]*>[^<]*</td>\s*<td[^>]*>([\d.,]+)</td>",
        html,
        re.IGNORECASE,
    )
    if not match:
        raise ValueError("Не удалось получить курс евро")

    eur_rate = float(match.group(1).replace(",", "."))

    # 2. Функция для замены
    def replace_amount(m):
        amount_rub = float(m.group(1))
        amount_eur = amount_rub / eur_rate
        return f"{amount_eur:,.2f} €"  # заменяем на евро

    # 3. Ищем все вхождения "<число> руб" (руб, рублей, RUB и т.д.)
    new_text = re.sub(r"(\d+(?:[.,]\d+)?)\s*(?:руб|р|rub)\b", replace_amount, text, flags=re.IGNORECASE)

    return new_text

text = "У меня есть 1500 руб и ещё 200 руб."
converted_text = convert_rub_to_eur_in_text(text)
print(converted_text)