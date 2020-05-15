"""
Главный модуль
"""

import tkinter as tk

from tkinter import Tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter.ttk import Treeview
from tkinter import messagebox

import sys
import os
sys.path.insert(0, os.getcwd())
print(sys.path)

import config
import analyse
from lib import db
from lib import validator


class MainWindow:
    """
    Класс главного окна
    """

    def __init__(self, top=None):
        """
        Создание всех элементов окна
        """

        top.geometry("1200x570+120+20")
        top.title("Football Analyser")
        top.configure(background=config.background_color)
        top.configure(highlightbackground=config.background_color)
        top.configure(highlightcolor="black")

        self.tree_view = Treeview(top, show="headings")

        self.first_name_label = Label(top)
        self.last_name_label = Label(top)
        self.country_label = Label(top)
        self.age_label = Label(top)
        self.plays_label = Label(top)
        self.goals_label = Label(top)

        self.first_name_entry = Entry(top)
        self.last_name_entry = Entry(top)
        self.country_entry = Entry(top)
        self.age_entry = Entry(top)
        self.plays_entry = Entry(top)
        self.goals_entry = Entry(top)

        self.entries_list = [self.first_name_entry, self.last_name_entry, self.country_entry, self.age_entry,
                             self.plays_entry, self.goals_entry]

        self.add_button = Button(top)
        self.delete_button = Button(top)
        self.modify_button = Button(top)
        self.clear_fields_button = Button(top)
        self.analyze_button = Button(top)

        self.configure_tree_view()\
            .configure_labels()\
            .configure_entries()\
            .configure_buttons()\
            .fill_on_start()

    def configure_tree_view(self):
        """
        Настройка treeview для отображения всех записей
        """

        self.tree_view.place(relx=0.008, rely=0.018, relheight=0.837, relwidth=0.754)

        self.tree_view["columns"] = ("First name", "Last name", "Country", "Age", "Plays", "Goals")

        self.tree_view.column("First name", width=200)
        self.tree_view.column("Last name", width=200)
        self.tree_view.column("Country", width=100)
        self.tree_view.column("Age", width=100)
        self.tree_view.column("Plays", width=100)
        self.tree_view.column("Goals", width=100)

        self.tree_view.heading("First name", text="First name")
        self.tree_view.heading("Last name", text="Last name")
        self.tree_view.heading("Country", text="Country")
        self.tree_view.heading("Age", text="Age")
        self.tree_view.heading("Plays", text="Plays")
        self.tree_view.heading("Goals", text="Goals")

        self.tree_view.bind("<<TreeviewSelect>>", lambda event: self.on_select_item())

        return self

    def configure_labels(self):
        """
        Настройка текста над полями ввода
        """

        self.first_name_label.place(relx=0.775, rely=0.07, height=26, width=74)
        self.first_name_label.configure(background=config.background_color)
        self.first_name_label.configure(text="First name")

        self.last_name_label.place(relx=0.775, rely=0.193, height=26, width=73)
        self.last_name_label.configure(background=config.background_color)
        self.last_name_label.configure(text="Last name")

        self.country_label.place(relx=0.775, rely=0.316, height=26, width=57)
        self.country_label.configure(background=config.background_color)
        self.country_label.configure(text="Country")

        self.age_label.place(relx=0.775, rely=0.439, height=26, width=33)
        self.age_label.configure(background=config.background_color)
        self.age_label.configure(text="Age")

        self.plays_label.place(relx=0.775, rely=0.561, height=26, width=39)
        self.plays_label.configure(background=config.background_color)
        self.plays_label.configure(text="Plays")

        self.goals_label.place(relx=0.775, rely=0.684, height=26, width=43)
        self.goals_label.configure(background=config.background_color)
        self.goals_label.configure(text="Goals")

        return self

    def configure_entries(self):
        """
        Настройка полей ввода
        """

        self.first_name_entry.place(relx=0.775, rely=0.123, height=24, relwidth=0.17)
        self.first_name_entry.configure(font=config.font)

        self.last_name_entry.place(relx=0.775, rely=0.246, height=24, relwidth=0.17)
        self.last_name_entry.configure(font=config.font)

        self.country_entry.place(relx=0.775, rely=0.368, height=24, relwidth=0.17)
        self.country_entry.configure(font=config.font)

        self.age_entry.place(relx=0.775, rely=0.491, height=24, relwidth=0.17)
        self.age_entry.configure(font=config.font)

        self.plays_entry.place(relx=0.775, rely=0.614, height=24, relwidth=0.17)
        self.plays_entry.configure(font=config.font)

        self.goals_entry.place(relx=0.775, rely=0.737, height=24, relwidth=0.17)
        self.goals_entry.configure(font=config.font)

        return self

    def configure_buttons(self):
        """
        Настройка кнопок
        """

        self.add_button.place(relx=0.792, rely=0.807, height=33, width=40)
        self.add_button.configure(background=config.background_color)
        self.add_button.configure(text="Add")
        self.add_button.configure(command=self.add_item)

        self.delete_button.place(relx=0.9, rely=0.807, height=33, width=56)
        self.delete_button.configure(background=config.background_color)
        self.delete_button.configure(text="Delete")
        self.delete_button.configure(command=self.delete_item)

        self.modify_button.place(relx=0.842, rely=0.807, height=33, width=59)
        self.modify_button.configure(background=config.background_color)
        self.modify_button.configure(text="Modify")
        self.modify_button.configure(command=self.modify_item)

        self.clear_fields_button.place(relx=0.8, rely=0.895, height=33, width=166)
        self.clear_fields_button.configure(background=config.background_color)
        self.clear_fields_button.configure(text="Clear fields")
        self.clear_fields_button.configure(command=self.clear_all_entries)

        self.analyze_button.place(relx=0.225, rely=0.877, height=53, width=336)
        self.analyze_button.configure(background=config.background_color)
        self.analyze_button.configure(text="Analyze")
        self.analyze_button.configure(font="-size 18")
        self.analyze_button.configure(command=self.analyze)

        return self

    def fill_on_start(self):
        """
        Заполнение treeview записями из базы данных
        """

        for row in db.get_records():
            self.tree_view.insert("", tk.END, values=row)
        return self

    def on_select_item(self):
        """
        Отображение выбранной записи в полях ввода для редактирования
        """

        values = self.tree_view.item(self.tree_view.focus())["values"]
        for entry, val in zip(self.entries_list, values):
            entry.delete(0, tk.END)
            entry.insert(0, val)

    def clear_all_entries(self):
        """
        Очистка всех полей ввода
        """

        for entry in self.entries_list:
            entry.delete(0, tk.END)

    def delete_item(self):
        """
        Удаление записи
        """

        item = self.tree_view.focus()
        db.delete_record(self.tree_view.index(item))
        self.tree_view.delete(item)
        self.clear_all_entries()

    def add_item(self):
        """
        Добавление записи
        """

        try:
            first_name = validator.validate_text(self.first_name_entry.get())
            last_name = validator.validate_text(self.last_name_entry.get())
            country = validator.validate_text(self.country_entry.get())
            age = validator.validate_number(self.age_entry.get())
            plays = validator.validate_number(self.plays_entry.get())
            goals = validator.validate_number(self.goals_entry.get())

            db.insert_record({
                "first_name": first_name,
                "last_name": last_name,
                "country": country,
                "age": age,
                "plays": plays,
                "goals": goals
            })
            self.tree_view.insert("", tk.END, values=(first_name, last_name, country, age, plays, goals))

        except ValueError:
            messagebox.showerror("Invalid input", "Input are not valid string or number")

        self.on_select_item()

    def modify_item(self):
        """
        Изменение записи
        """

        try:
            item = self.tree_view.focus()
            index = self.tree_view.index(item)

            first_name = validator.validate_text(self.first_name_entry.get())
            last_name = validator.validate_text(self.last_name_entry.get())
            country = validator.validate_text(self.country_entry.get())
            age = validator.validate_number(self.age_entry.get())
            plays = validator.validate_number(self.plays_entry.get())
            goals = validator.validate_number(self.goals_entry.get())

            db.update_record(index, (first_name, last_name, country, age, plays, goals))
            self.tree_view.item(item, values=(first_name, last_name, country, age, plays, goals))

        except ValueError:
            messagebox.showerror("Invalid input", "Input are not valid string or number")

        self.on_select_item()

    def analyze(self):
        """
        Вызов анализа
        """

        analyse.full_analysis()
        messagebox.showinfo("Done", "Файлы отчета сохранены в output и graphics")


def main():
    """
    Метод запуска, загружает базу данных и открывает окно
    """

    db.load_dataframe(config.db_players_path, config.db_plays_path)
    root = Tk()
    MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
