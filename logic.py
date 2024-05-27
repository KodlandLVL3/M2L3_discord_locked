from discord import ui, ButtonStyle


class Question:
    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    @property
    def text(self):
        return self.__text 

    def gen_buttons(self):
        buttons = []
        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'correct_{i}'))
            else:
                buttons.append(ui.Button(label=option, style=ButtonStyle.primary, custom_id=f'wrong_{i}'))
        return buttons


quiz_questions = [
    Question("Что котики делают, когда никто их не видит?", 1, "Спят", "Пишут мемы"),
    Question("Как котики выражают свою любовь?", 0, "Громким мурлыканием", "Отправляют фото на Instagram", "Гавкают"),
    Question("Какие книги котики любят читать?", 3, "Обретение вашего внутреннего урр-мирения", "Тайм-менеджмент или как выделить 18 часов в день для сна", "101 способ уснуть на 5 минут раньше, чем хозяин", "Пособие по управлению людьми")
]
