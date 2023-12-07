import sqlite3

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog  # QMetaObject
from PyQt5.QtGui import QPixmap


class Character(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi('blank.ui', self)

        # Коннектимся с БД
        self.con = sqlite3.connect('db\my_db1.db')
        self.cur = self.con.cursor()

        # Подгружаем аватарку по умолчанию
        self.filename = 'images/ava.png'
        self.pixmap = QPixmap(self.filename)
        self.photo.setPixmap(self.pixmap)

        # Список всех полей для работы с базой данных
        self.all_widgets = (self.character_name,
                            self.EXP,
                            self.LVL,
                            self.HP,
                            self.DEF,
                            self.zz,
                            self.character_history,
                            self.character_class,
                            self.race,
                            self.photo,
                            self.inventory,
                            self.language,
                            self.character_state,
                            self.power,
                            self.dexterity,
                            self.intelligence,
                            self.body,
                            self.charisma,
                            self.wisdom,
                            self.money_copper,
                            self.money_gold,
                            self.money_silver,
                            self.money_platinum,
                            self.atacs,
                            self.main_history,
                            self.power_savingroll,
                            self.power_savingroll_num,
                            self.athletics,
                            self.athletics_num,
                            self.dexterity_savingroll,
                            self.dexterity_savingroll_num,
                            self.acrobatics,
                            self.acrobatics_num,
                            self.prestidigitation,
                            self.prestidigitation_num,
                            self.secrecy,
                            self.secrecy_num,
                            self.intellect_savingroll,
                            self.intellect_savingroll_num,
                            self.magic,
                            self.magic_num,
                            self.history,
                            self.history_num,
                            self.analysis,
                            self.analysis_num,
                            self.nature,
                            self.nature_num,
                            self.religion,
                            self.religion_num,
                            self.body_savingroll,
                            self.body_savingroll_num,
                            self.charisma_savingroll,
                            self.charisma_savingroll_num,
                            self.deceit,
                            self.deceit_num,
                            self.intimidation,
                            self.intimidation_num,
                            self.performance,
                            self.performance_num,
                            self.belief,
                            self.belief_num,
                            self.wisdom_savingroll,
                            self.wisdom_savingroll_num,
                            self.animal_care,
                            self.animal_care_num,
                            self.insight,
                            self.insight_num,
                            self.medicine,
                            self.medicine_num,
                            self.attention,
                            self.attention_num,
                            self.survival,
                            self.survival_num)

        self.saved_pers()

        # Выбор персонажа из выпадающего списка [pers]
        self.pers.currentTextChanged.connect(self.load)

        # Принудительное обновление списка персонажей
        self.btn_refresh_pers_list.clicked.connect(self.saved_pers)

        # Кнопки для работы с изображениями
        self.load_img_btn.clicked.connect(self.img_load)
        self.delite_img_btn.clicked.connect(self.img_delite)

        # Стандартные кнопки [Сохранить] [Удалить] [Очистить]
        self.btn_clean.clicked.connect(self.clean)
        self.btn_delite.clicked.connect(self.delete)
        self.btn_save.clicked.connect(self.save)

        # Денежные кнопки
        self.copper_plus.clicked.connect(self.money)
        self.copper_minus.clicked.connect(self.money)
        self.silver_plus.clicked.connect(self.money)
        self.silver_minus.clicked.connect(self.money)
        self.gold_plus.clicked.connect(self.money)
        self.gold_minus.clicked.connect(self.money)
        self.platinum_plus.clicked.connect(self.money)
        self.platinum_minus.clicked.connect(self.money)

    def saved_pers(self):
        '''Добавление в выпадающий список существующих персонажей всех персонажей из таблицы [characters]'''
        AllItems = [self.pers.itemText(i) for i in range(self.pers.count())]
        name = self.cur.execute("SELECT character_name FROM characters").fetchall()

        for i in name:
            if i not in AllItems:
                self.pers.addItem(i[0])    # str()