# extractor/utils.py
import re
import dateparser


def normalize_date(date_str):
    date_obj = dateparser.parse(date_str, region='RU', locales=['ru'])
    if date_obj:
        return date_obj.strftime("%d.%m.%Y")
    return date_str  # Если формат не распознан, возвращаем оригинальную строку


def normalize_term(term_str):
    term_str = term_str.lower()
    years = re.search(r"(\d+)\s*г", term_str)
    months = re.search(r"(\d+)\s*м", term_str)
    weeks = re.search(r"(\d+)\s*н", term_str)
    days = re.search(r"(\d+)\s*д", term_str)

    result = "_".join([
        str(years.group(1)) if years else "0",
        str(months.group(1)) if months else "0",
        str(weeks.group(1)) if weeks else "0",
        str(days.group(1)) if days else "0",
    ])

    return result