import json


class CategoryNode:
    categoty_id = 0

    def __init__(self, name):
        CategoryNode.categoty_id += 1
        self.id = CategoryNode.categoty_id
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def to_dict(self):
        # Рекурсивно преобразовываем структуру в словарь
        return {
            'id': self.id,
            'name': self.name,
            'children': [child.to_dict() for child in self.children]
        }


def generate_location_indent(indent):
    return " " * indent


def get_category_tree():
    all_categories = CategoryNode("Все категории")

    raw_locations = {
        "Бытовая электроника": ["Товары для компьютера", "Фототехника", "Телефоны", "Планшеты и электронные книги",
                                "Оргтехника и расходники", "Ноутбуки", "Настольные компьютеры",
                                "Игры, приставки и программы", "Аудио и видео"],
        "Готовый бизнес и оборудование": ["Готовый бизнес", "Оборудование для бизнеса"],
        "Для дома и дачи": ["Мебель и интерьер", "Ремонт и строительство", "Продукты питания", "Растения",
                            "Бытовая техника", "Посуда и товары для кухни"],
        "Животные": ["Другие животные", "Товары для животных", "Птицы", "Аквариум", "Кошки", "Собаки"],
        "Личные вещи": ["Детская одежда и обувь", "Одежда, обувь, аксессуары", "Товары для детей и игрушки",
                        "Часы и украшения", "Красота и здоровье"],
        "Недвижимость": ["Недвижимость за рубежом", "Квартиры", "Коммерческая недвижимость", "Гаражи и машиноместа",
                         "Земельные участки", "Дома, дачи, коттеджи", "Комнаты"],
        "Работа": ["Резюме", "Вакансии"],
        "Транспорт": ["Автомобили", "Запчасти и аксессуары", "Грузовики и спецтехника", "Водный транспорт",
                      "Мотоциклы и мототехника"],
        "Услуги": ["Предложения услуг"],
        "Хобби и отдых": ["Охота и рыбалка", "Спорт и отдых", "Коллекционирование", "Книги и журналы", "Велосипеды",
                          "Музыкальные инструменты", "Билеты и путешествия"]
    }

    for category, subcategories in raw_locations.items():
        category_node = CategoryNode(category)

        for subcategory in subcategories:
            subcategory_node = CategoryNode(subcategory)
            category_node.add_child(subcategory_node)

        all_categories.add_child(category_node)

    return all_categories


# Получаем словарь из дерева и сериализуем его в JSON


category_tree = get_category_tree()
categories_dict = category_tree.to_dict()
new_json = json.dumps(categories_dict, ensure_ascii=False, indent=4)