"""
Анализ данных
"""


import matplotlib.pyplot as plt
import config
from lib import db


def countries_pie_chart(data):
    """
    Построение круговой диаграммы для процентного соотношения по странам
    """

    plt.clf()
    chart = {}
    for el in data:
        if el[2] in chart:
            chart[el[2]] += 1
        else:
            chart[el[2]] = 1
    plt.pie(chart.values(), labels=chart.keys(), autopct='%1.1f%%', shadow=True, startangle=140)

    plt.axis('equal')
    plt.title("Процетное соотношение по странам\n")
    plt.savefig(f"{config.graphics_dir}/countries.png")


def ages_hist(data):
    """
    Построение гистограммы по возрастам
    """

    plt.clf()
    ages = [el[3] for el in data]
    plt.hist(ages, len(ages))
    plt.title("Количественное соотношение по возрастам")
    plt.ylabel("Количество")
    plt.xlabel("Возраст")
    plt.savefig(f"{config.graphics_dir}/ages.png")


def text_report(data):
    """
    Текстовый отчет с основной информацией
    """

    most_efficient = sorted(data, key=lambda el: el[5]/el[4], reverse=True)[0]
    sorted_by_age = sorted(data, key=lambda el: el[3])
    youngest, oldest = sorted_by_age[0], sorted_by_age[-1]

    with open(f"{config.output_dir}/report.txt", mode="w", encoding="utf-8") as file:
        file.write(f"Всего записей: {len(data)}\n")
        file.write(f"Лучший игрок: {most_efficient[0]} {most_efficient[1]} ({most_efficient[4]} игр, {most_efficient[5]} голов)\n")
        file.write(f"Самый молодой: {youngest[0]} {youngest[1]} ({youngest[3]} лет/года)\n")
        file.write(f"Самый старый: {oldest[0]} {oldest[1]} ({oldest[3]} лет/года)")


def full_analysis():
    """
    Полный анализ
    """

    data = db.get_records()
    countries_pie_chart(data)
    ages_hist(data)
    text_report(data)
