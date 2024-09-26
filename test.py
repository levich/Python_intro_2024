import re


def isCyrillic(text):
    return bool(re.search('[а-яА-Я]', text))


def calc_points(text):
    points_en = {1: 'AEIOULNSTR',
                 2: 'DG',
                 3: 'BCMP',
                 4: 'FHVWY',
                 5: 'K',
                 8: 'JZ',
                 10: 'QZ'}
    points_ru = {1: 'АВЕИНОРСТ',
                 2: 'ДКЛМПУ',
                 3: 'БГЁЬЯ',
                 4: 'ЙЫ',
                 5: 'ЖЗХЦЧ',
                 8: 'ШЭЮ',
                 10: 'ФЩЪ'}
    if isCyrillic(text):
        return sum([k for i in text for k, v in points_ru.items() if i in v])
    else:
        return sum([k for i in text for k, v in points_en.items() if i in v])


# l = ["Privet", "Apple", "Mac", "Answer", "Demo", "Open", "if",
#      "Nickelback", "Яблоко", "Привет", "Автор", "Эзофагодуоденоэндоскопия", "asd asd asd"]
# for e in l:
#     print(e, calc_points(e))
# Задача организации, в особенности же сплочённость команды профессионалов способствует подготовке и реализации системы обучения кадров, соответствующей насущным потребностям. Учитывая ключевые сценарии поведения, укрепление и развитие внутренней структуры говорит о возможностях экспериментов, поражающих по своей масштабности и грандиозности. В частности, постоянный количественный рост и сфера нашей активности требует определения и уточнения системы массового участия.

print(calc_points(input()))