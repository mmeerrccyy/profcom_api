from django.core.management import BaseCommand
from django.core.management.color import no_style
from django.db import connection
from django.db.models import RestrictedError

from resumes_vacancies.models import DirectionsModel, WorkTimeModel, DegreeModel, ExperienceModel, EnglishLevelModel


class Command(BaseCommand):
    __directions = (
        'IT, комп\'ютери, інтернет',
        'Адмiнiстрацiя, керівництво середньої ланки',
        'Будівництво, архітектура',
        'Бухгалтерія, аудит, секретаріат, діловодство, АГВ',
        'Готельно-ресторанний бізнес, туризм, сфера обслуговування',
        'Дизайн, творчість',
        'ЗМІ, видавництво, поліграфія',
        'Краса, фітнес, спорт',
        'Культура, музика, шоу-бізнес',
        'Логістика, склад, ЗЕД',
        'Маркетинг, реклама, PR, телекомунікації та зв\'язок',
        'Медицина, фармацевтика',
        'Нерухомість',
        'Освіта, наука',
        'Охорона, безпека',
        'Продаж, закупівля',
        'Робочі спеціальності, виробництво',
        'Роздрібна торгівля',
        'Сільське господарство, агробізнес',
        'Транспорт, автобізнес',
        'Фінанси, банк',
        'Управління персоналом, HR',
        'Юриспруденція',
    )

    __work_times = (
        'Повний робочий день',
        'Неповний робочий день/часткова зайнятість',
        'Фріланс/разовий проєкт',
        'Позмінний графік',
    )

    __degrees = (
        'Не завершена вища (студент)',
        'Неповна вища (бакалавр)',
        'Повна вища (магістр)',
        'Випускник',
    )

    __experience = (
        'Без досвіду роботи',
        'Досвід роботи в іншій сфері',
        'Менше 1 року',
        '1+ року',
        '2+ роки',
    )

    __english_level = (
        'A1-A2',
        'B1',
        'B2',
        'C1-C2',
    )

    def handle(self, *args, **options):
        try:
            models = (DirectionsModel, WorkTimeModel, DegreeModel, ExperienceModel, EnglishLevelModel)
            entities_names = (self.__directions, self.__work_times, self.__degrees, self.__experience,
                              self.__english_level)

            for model in models:
                model.objects.all().delete()

            sequence_sql = connection.ops.sequence_reset_sql(no_style(), models)
            with connection.cursor() as cursor:
                for sql in sequence_sql:
                    cursor.execute(sql)

            for model_group in zip(models, entities_names):
                model = model_group[0]
                for entity_name in model_group[1]:
                    entity = model(
                        None, entity_name
                    )
                    entity.save()
                    print(f'Entity added to {model.__name__}:', entity_name)
            print('Finish')

        except RestrictedError as exc:
            print('Error occurred: ', exc)
