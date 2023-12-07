import sqlite3
from const import ZERO_PERS


def create_db():
    # Коннектимся с БД, если ее не существует: создаем ее
    db = sqlite3.connect('db\my_db1.db')
    cur = db.cursor()

    # Создаем таблицу [characters] В БД, если ее не существует
    cur.execute('''CREATE TABLE IF NOT EXISTS characters (
        character_name TEXT PRIMARY KEY,
        EXP TEXT,
        LVL TEXT,
        HP TEXT,
        DEF TEXT,
        zz TEXT,
        character_history TEXT,
        character_class TEXT,
        race TEXT,
        photo TEXT,
        language TEXT,
        atacs TEXT,
        main_history TEXT,
        money_copper TEXT,
        money_silver TEXT,
        money_gold TEXT,
        money_platinum TEXT,
        power TEXT,
        dexterity TEXT,
        intelligence TEXT,
        body TEXT,
        charisma TEXT,
        wisdom TEXT,
        inventory TEXT,
        character_state TEXT,
        power_savingroll TEXT,
        power_savingroll_num TEXT,
        athletics TEXT,
        athletics_num TEXT,
        dexterity_savingroll TEXT,
        dexterity_savingroll_num TEXT,
        acrobatics TEXT,
        acrobatics_num TEXT,
        prestidigitation TEXT,
        prestidigitation_num TEXT,
        secrecy TEXT,
        secrecy_num TEXT,
        intellect_savingroll TEXT,
        intellect_savingroll_num TEXT,
        magic TEXT,
        magic_num TEXT,
        history TEXT,
        history_num TEXT,
        analysis TEXT,
        analysis_num TEXT,
        nature TEXT,
        nature_num TEXT,
        religion TEXT,
        religion_num TEXT,
        body_savingroll TEXT,
        body_savingroll_num TEXT,
        charisma_savingroll TEXT,
        charisma_savingroll_num TEXT,
        deceit TEXT,
        deceit_num TEXT,
        intimidation TEXT,
        intimidation_num TEXT,
        performance TEXT,
        performance_num TEXT,
        belief TEXT,
        belief_num TEXT,
        wisdom_savingroll TEXT,
        wisdom_savingroll_num TEXT,
        animal_care TEXT,
        animal_care_num TEXT,
        insight TEXT,
        insight_num TEXT,
        medicine TEXT,
        medicine_num TEXT,
        attention TEXT,
        attention_num TEXT,
        survival TEXT,
        survival_num TEXT)''')

    db.commit()

    name = cur.execute("SELECT character_name FROM characters").fetchall()

    if ('',) not in name:
        cur.execute(f'''INSERT INTO characters (character_name, EXP, LVL, HP, DEF, zz, character_history,
        character_class, race, photo, language, atacs, main_history, money_copper, money_gold, money_silver, 
        money_platinum, power, dexterity, intelligence, body, charisma, wisdom, inventory, character_state, 
        power_savingroll,
        power_savingroll_num, athletics, athletics_num, dexterity_savingroll, dexterity_savingroll_num, acrobatics,
        acrobatics_num, prestidigitation, prestidigitation_num, secrecy, secrecy_num, intellect_savingroll,
        intellect_savingroll_num, magic, magic_num, history, history_num, analysis, analysis_num, nature,
        nature_num, religion, religion_num, body_savingroll, body_savingroll_num, charisma_savingroll,
        charisma_savingroll_num, deceit, deceit_num, intimidation, intimidation_num, performance,
        performance_num, belief, belief_num, wisdom_savingroll, wisdom_savingroll_num, animal_care,
        animal_care_num, insight, insight_num, medicine, medicine_num, attention, attention_num, survival, survival_num)
        VALUES{ZERO_PERS}''')

        db.commit()
