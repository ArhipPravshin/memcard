'''ЗАГРУЗКА БИБЛИОТЕК'''
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle, randint
 
'''СОЗДАНИЕ КЛАССА, КОТОРЫЙ БУДЕТ СОХРАНЯТЬ ВОПРОСЫ И ОТВЕТЫ'''
 
class Question():
    ''' содержит вопрос, правильный ответ и три неправильных'''
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        # все строки надо задать при создании объекта, они запоминаются в свойства
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
'''ДОБАВЛЕНИЕ ВАРИАНТОВ ОТВЕТА'''
questions_list = [] #создание спика для хранения вопросов
questions_list.append(Question('Какое значение принимает функция sin(x) при x = 90 градусов?', '1', '0', '-1', '2sqrt(3)'))
questions_list.append(Question('Чем отличается борщевик сосновского от других видов борщевика?', 'Он ядовитый, а другие нет ', 'он не ядовитый, а другие да', 'Он абсолютно безопасен', 'Вся Москва не заросла этой дрянью'))
questions_list.append(Question('Что произошло 1 февраля 2003 года?', 'Трагедия шаттла Колумбия', 'Ничего', 'Революция в США', 'Была солнечная погода'))
questions_list.append(Question('Правда ли, что люди были на Луне, а если были, то к какой стране принадлежали?', 'Да, США', 'Нет', 'Да, СССР', 'Да, Люксембург'))
questions_list.append(Question('Какая мощность царь-бомбы должная была получится, но испыьали ослабленную версию?(в мегатоннах)', '100', '58', '1500', '3'))
questions_list.append(Question('Чьи фамилии упоминаются в гимне СССР?', 'Сталин, Ленин', 'Ленин', 'Сталин', 'Путин'))
questions_list.append(Question('Самый большой вулкан:', 'Олимп', 'Ключевская Сопка', 'Эверест', 'Титикака'))
questions_list.append(Question('Почему полёт SLS в программе миссий Артемида откладывали 3 раза (3 чёртовых раза из-за одной и той-же проблемы)', 'Риск утечки водорода', 'Топливо попало в двигатель', 'Плутон стал планетой (эх мечты мечты)', 'Риск утечки гидролокса'))
questions_list.append(Question('Почему Плутон больше не планета?', 'Он не доминирует на своей орбите', 'Потому-что', 'Харон так сказал', 'Его уменьшили лягушки, так как Германия напала на Люксембург!!!!'))
questions_list.append(Question('Какая теория верна?', 'ОТО', 'Теория струн', 'Закон Всемирного Тяготения', 'Теория о страпельках'))
questions_list.append(Question('Масса искажает пространство-время?', 'Да', 'Нет', 'не знаю', 'Скорее НЕТ, чем ДА'))
questions_list.append(Question('Отличия термоядерной и ядерной реакции', 'В ядерной реакции скопление частиц + маленькая частица = E + много маленьких, а термоядерной наоборот', 'Я не знаю', 'Приставка термо-', 'Их нет'))
questions_list.append(Question('Слово "нету" есть в русском языке?', 'Нет', 'Да', 'Естественно', 'Конечно'))
questions_list.append(Question('Да?', 'поезда', 'да?', 'аД', 'дА'))
questions_list.append(Question('Дорогие бренды одежды - это просто развод лохов на бабки или мы просто не понимаем?', 'Это развод лохов на бабки', 'Мы не понимаем, это же не для бедных и тд', 'Я не знаю', 'четвёртый вариант ответа'))
questions_list.append(Question('Кодзима гений?', 'Гений', 'Нет', 'Я не знаю', 'Кто это?'))
questions_list.append(Question('Внешний долг США:', '14 трлн долларов', '1 копейка', 'Я не знаю', '20 грiвен'))
questions_list.append(Question('Гарри Ньюмен легенда?', 'Да', 'нет', 'кто это?', 'четвёртый вариант ответа'))

'''СОЗДАНИЕ ОСНОВНЫХ ВИДЖЕТОВ'''
 
app = QApplication([]) #приложение
btn_OK = QPushButton('Ответить') #кнопка
lb_Question = QLabel('Самый сложный вопрос в мире!') #текст вопроса
 
'''СОЗДАНИЕ И НАСТРОЙКА ГРУППЫ ВОПРОСОВ'''
 
RadioGroupBox = QGroupBox("Варианты ответов") #создание группы для объединения виджетов
 
rbtn_1 = QRadioButton('Вариант 1') #создание кнопок-переключателей
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')
 
RadioGroup = QButtonGroup() #создание группы для объединения кнопок
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout() #создание направляющих линий
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) #добавление кнопок к направляющим линиям
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2) #добавление вертикальных линий с кнопками к основной горизонтальной линни
layout_ans1.addLayout(layout_ans3)
 
RadioGroupBox.setLayout(layout_ans1) #добавление горизонтальной линии со всеми кнопками в группу-виджет
 
'''СОЗДАНИЕ И НАСТРОЙКА ГРУППЫ ОТВЕТОВ'''  
 
AnsGroupBox = QGroupBox("Результат теста")  #создание группы для объединения виджетов
lb_Result = QLabel('прав ты или нет?')  #виджеты с надписями
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout() #создание вертикальной линии
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop)) #добавление нужных виджетов и настройка расположения
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res) #добавление вертикального линия в группу для виджетов
 
'''НАСТРОЙКА ВНЕШНЕГО ВИДА ОСНОВНОГО ОКНА'''
 
layout_line1 = QHBoxLayout() #направляющие линии
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) #прикрепление виджетов к направлющим линиям
layout_line2.addWidget(RadioGroupBox)  
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() #скрытие группы ответов
 
layout_line3.addStretch(1) #настройка внешнего вида
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
layout_card = QVBoxLayout() #создание главной направляющей
 
layout_card.addLayout(layout_line1, stretch=2) #прикрепление вторичных направляющих к главной и их настройка
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
 
'''ФУНКЦИИ ДЛЯ ОБРАБОТКИ ОТВЕТОВ'''
 
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4] # установка кнопок-переключателей в список
 
def show_result(res):
    ''' показать результат - установим переданный текст в надпись "результат" и покажем нужную панель '''
    lb_Result.setText(res)
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')
 
 
def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана
 
def check_answer():
    ''' если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_result('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_result('Неверно! Иди учи уроки а не гдз')
 
def check_btn(): #проверка нажатия нужной кнопки
    if 'Ответить' == btn_OK.text():
        check_answer()
    else:
        next_question()
       
def ask(q: Question):
    ''' функция записывает значения вопроса и ответов в соответствующие виджеты,
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer) # первый элемент списка заполним правильным ответом, остальные - неверными
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # вопрос
    lb_Correct.setText(q.right_answer)
    show_question()
 
def next_question():
    ''' задает следующий вопрос из списка '''
    # этой функции нужна переменная, в которой будет указываться номер текущего вопроса
    # эту переменную можно сделать глобальной, либо же сделать свойством "глобального объекта" (app или window)
    # мы заведем (ниже) свойство window.cur_question.
    window.total += 1
    print('Статистика\n-Всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0, len(questions_list) - 1)  # нам не нужно старое значение, 
                                                        # поэтому можно использовать локальную переменную! 
            # случайно взяли вопрос в пределах списка
            # если внести около сотни слов, то редко будет повторяться
    q = questions_list[cur_question] # взяли вопрос
    ask(q) # спросили
 
 
'''СОЗДАНИЕ И НАСТРОЙКА ОКНА'''
window = QWidget()
 #создание нового свойства окна для нумерации вопросов
window.score = 0
window.total = 0
window.setLayout(layout_card) #добавление в окно главного виджета
window.setWindowTitle('Memo Card')
window.resize(400, 300)
 
next_question()
btn_OK.clicked.connect(check_btn) # проверяем, что панель ответов показывается при нажатии на кнопку
 
window.show()
app.exec()
