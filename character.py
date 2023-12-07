import sqlite3

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog  # QMetaObject
from PyQt5.QtGui import QPixmap

from const import CHARACTER_COLUMN, ZERO_PERS


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
        self.load_img_btn.clicked.connect(self.img_choice)
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
                self.pers.addItem(i[0])  # str()

    def money(self):
        '''Изменение количества монет'''
        btn = QApplication.instance().sender()
        if btn == self.copper_plus:
            a = int(self.money_copper.text()) + int(self.append_money_copper.text())
            self.money_copper.setText(str(a))
            self.append_money_copper.setText('0')
        elif btn == self.copper_minus:
            a = int(self.money_copper.text()) - int(self.append_money_copper.text())
            self.money_copper.setText(str(a))
            self.append_money_copper.setText('0')
        elif btn == self.silver_plus:
            a = int(self.money_silver.text()) + int(self.append_money_silver.text())
            self.money_silver.setText(str(a))
            self.append_money_silver.setText('0')
        elif btn == self.silver_minus:
            a = int(self.money_silver.text()) - int(self.append_money_silver.text())
            self.money_silver.setText(str(a))
            self.append_money_silver.setText('0')
        elif btn == self.gold_plus:
            a = int(self.money_gold.text()) + int(self.append_money_gold.text())
            self.money_gold.setText(str(a))
            self.append_money_gold.setText('0')
        elif btn == self.gold_minus:
            a = int(self.money_gold.text()) - int(self.append_money_gold.text())
            self.money_gold.setText(str(a))
            self.append_money_gold.setText('0')
        elif btn == self.platinum_plus:
            a = int(self.money_platinum.text()) + int(self.append_money_platinum.text())
            self.money_platinum.setText(str(a))
            self.append_money_platinum.setText('0')
        elif btn == self.platinum_minus:
            a = int(self.money_platinum.text()) - int(self.append_money_platinum.text())
            self.money_platinum.setText(str(a))
            self.append_money_platinum.setText('0')

    def img_choice(self):
        '''Выбор изображение персонажа при нажатии кнопки [загрузить изображение]'''
        self.filename = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '/images',
                                                    'Картинка (*.jpg);;Картинка (*.png);;Все файлы (*)')[0]
        self.img_load()

    def img_load(self):
        pixmap = QPixmap(self.filename)

        # масштабирование изображения под размер 171*171
        pixmap_scaled = pixmap.scaled(171, 171, QtCore.Qt.KeepAspectRatio)

        self.photo.setPixmap(pixmap_scaled)

    def img_delite(self):
        '''Заменить текущее изображение персонажа при нажатии кнопки [удалить изображение] на
        аватарку по умолчанию'''
        self.img_start()
        self.img_load()

    def img_start(self):
        self.filename = 'images/ava.png'

    def clean(self):
        '''Очистить лист по кнопке [Очистить]'''
        try:
            for i, walue in enumerate(ZERO_PERS):
                widget = self.all_widgets[i]
                typ = widget.metaObject().className()
                if typ == 'QLineEdit':
                    widget.setText(walue)
                elif typ == 'QSpinBox':
                    widget.setValue(int(walue))
                elif typ == 'QComboBox':
                    pass
                elif typ == 'QLabel':
                    widget.setText(walue)
                elif typ == 'QPlainTextEdit':
                    widget.setPlainText(walue)
                elif typ == 'QCheckBox':
                    widget.setChecked(bool(walue))
        except Exception as e:
            print(e)

    def load(self):
        '''Загрузить лист уже существующего персонажа [в выподающем меню]'''
        try:
            current_pers = self.pers.currentText()

            results = self.cur.execute(f'''SELECT * FROM characters
                                            WHERE character_name = "{current_pers}"''').fetchall()[0]

            for i, col in enumerate(CHARACTER_COLUMN):
                widget = self.all_widgets[i]
                typ = widget.metaObject().className()
                print(typ, widget, results[i])
                if typ == 'QLineEdit':
                    widget.setText(results[i])
                elif typ == 'QSpinBox':
                    widget.setValue(int(results[i]))
                elif typ == 'QComboBox':
                    pass
                elif typ == 'QLabel':
                    widget.setText(results[i])
                elif typ == 'QPlainTextEdit':
                    widget.setPlainText(results[i])
                elif typ == 'QCheckBox':
                    widget.setChecked(bool(results[i]))
        except Exception as e:
            print(e)

    def delete(self):
        '''Удаление персонажа при нажатии кнопки [Удалить]'''
        self.cur.execute(f'''DELETE from characters
                    WHERE character_name = "{self.character_name.text()}"''')

        self.con.commit()

        self.clean()
        self.saved_pers()

    def save(self):
        '''Сохранение персонажа при нажатии кнопки [Сохранить]'''
