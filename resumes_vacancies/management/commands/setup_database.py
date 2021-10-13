from django.core.management import BaseCommand
from django.core.management.color import no_style
from django.db import connection
from django.db.models import RestrictedError

from resumes_vacancies.models import DirectionsModel, WorkTimeModel


class Command(BaseCommand):
    __directions = [
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
    ]

    __work_times = [
        'Повна зайнятість',
        'Неповна зайнятість',
        'Дистанційна робота',
    ]

    def handle(self, *args, **options):
        try:
            DirectionsModel.objects.all().delete()
            WorkTimeModel.objects.all().delete()

            sequence_sql = connection.ops.sequence_reset_sql(no_style(), [DirectionsModel, WorkTimeModel])
            with connection.cursor() as cursor:
                for sql in sequence_sql:
                    cursor.execute(sql)

            for i in self.__directions:
                entity = DirectionsModel(
                    direction=i
                )
                entity.save()
                print('Added direction:', i)

            for i in self.__work_times:
                entity = WorkTimeModel(
                    work_time=i
                )
                entity.save()
                print('Added work time:', i)
            print('Finish')
        except RestrictedError:
            pass
