# Django REST Backend for Recruiting Website

## Installing

```shell
$ git clone https://github.com/mmeerrccyy/profcom_api.git
```

--------------------------

## Running

```shell
$ cd profcom_api
$ docker-compose up
```

Then docker will run PostgreSQL and Django containers.

Django will run on http://0.0.0.0:8080/

----------------

## API

There are 5 api urls:

- http://0.0.0.0:8080/api/work_times/ ([Work Time API](#Work-Time-API))
- http://0.0.0.0:8080/api/directions/ ([Directions API](#Directions-API))
- http://0.0.0.0:8080/api/vacancies/ ([Vacancies API](#Vacancies-API))
- http://0.0.0.0:8080/api/resumes/ ([Resumes API](#Resumes-API))
- http://0.0.0.0:8080/api/amount/ ([Amount of Vacancies and Resumes API](#Amount-of-Vacancies-and-Resumes-API))

-----------------

### Work Time API

ALLOW:

- GET

<details><summary>Fields:</summary>

- id (primary key)
- work_time

</details>

<details><summary>JSON GET Request</summary>

```json
[
  {
    "id": 1,
    "work_time": "Повна зайнятість"
  },
  {
    "id": 2,
    "work_time": "Неповна зайнятість"
  },
  {
    "id": 3,
    "work_time": "Дистанційна робота"
  }
]
```

</details>

------------------

### Directions API

ALLOW:

- GET

<details><summary>Fields:</summary>

- id (primary key)
- direction

</details>

<details> <summary>JSON GET Request</summary>

```json
[
  {
    "id": 1,
    "direction": "IT, комп'ютери, інтернет"
  },
  {
    "id": 2,
    "direction": "Адмiнiстрацiя, керівництво середньої ланки"
  },
  {
    "id": 3,
    "direction": "Будівництво, архітектура"
  },
  {
    "id": 4,
    "direction": "Бухгалтерія, аудит, секретаріат, діловодство, АГВ"
  },
  {
    "id": 5,
    "direction": "Готельно-ресторанний бізнес, туризм, сфера обслуговування"
  },
  {
    "id": 6,
    "direction": "Дизайн, творчість"
  },
  {
    "id": 7,
    "direction": "ЗМІ, видавництво, поліграфія"
  },
  {
    "id": 8,
    "direction": "Краса, фітнес, спорт"
  },
  {
    "id": 9,
    "direction": "Культура, музика, шоу-бізнес"
  },
  {
    "id": 10,
    "direction": "Логістика, склад, ЗЕД"
  },
  {
    "id": 11,
    "direction": "Маркетинг, реклама, PR, телекомунікації та зв'язок"
  },
  {
    "id": 12,
    "direction": "Медицина, фармацевтика"
  },
  {
    "id": 13,
    "direction": "Нерухомість"
  },
  {
    "id": 14,
    "direction": "Освіта, наука"
  },
  {
    "id": 15,
    "direction": "Охорона, безпека"
  },
  {
    "id": 16,
    "direction": "Продаж, закупівля"
  },
  {
    "id": 17,
    "direction": "Робочі спеціальності, виробництво"
  },
  {
    "id": 18,
    "direction": "Роздрібна торгівля"
  },
  {
    "id": 19,
    "direction": "Сільське господарство, агробізнес"
  },
  {
    "id": 20,
    "direction": "Транспорт, автобізнес"
  },
  {
    "id": 21,
    "direction": "Фінанси, банк"
  },
  {
    "id": 22,
    "direction": "Управління персоналом, HR"
  },
  {
    "id": 23,
    "direction": "Юриспруденція"
  }
]
```

</details>

--------------------

### Vacancies API

ALLOW:

- GET
- POST

<details> <summary>Fields:</summary>

- id (primary key)
- company_name (max length = 45) *
- company_short_description (text area)
- company_direction (foreign key to Directions) *
- vacancy_name (max length = 90) *
- vacancy_description (text area) *
- vacancy_requirements (text area) *
- vacancy_working_conditions (text area) *
- vacancy_salary (max length = 20)
- vacancy_benefits (text area)
- vacancy_contacts ()
- company_website
- vacancy_date_added

</details>

<details><summary>JSON GET Request</summary>

```json
[
  {
    "id": 1,
    "company_name": "Test Company",
    "company_short_description": "Test description",
    "vacancy_name": "Test vacancy name",
    "vacancy_description": "Test vacancy description",
    "vacancy_requirements": "Test",
    "vacancy_working_conditions": "Test",
    "vacancy_salary": "1000-2000$",
    "vacancy_benefits": "Test",
    "vacancy_contacts": "Test\r\nTest\r\nTest",
    "company_website": "Test.com\r\nTest.org\r\nTest.ua",
    "vacancy_date_added": "2021-10-14T17:44:20.597934Z",
    "company_direction": {
      "id": 6,
      "direction": "Дизайн, творчість"
    }
  },
  {
    "id": 2,
    "company_name": "Test Company 2",
    "company_short_description": "Test description 2",
    "vacancy_name": "Test vacancy name 2",
    "vacancy_description": "Test vacancy description 2",
    "vacancy_requirements": "Test 2",
    "vacancy_working_conditions": "Test 2",
    "vacancy_salary": "1000-2000$",
    "vacancy_benefits": "Test 2",
    "vacancy_contacts": "Test 2\r\nTest 2\r\nTest 2",
    "company_website": "Test.com 2 \r\nTest.org 2\r\nTest.ua 2",
    "vacancy_date_added": "2021-10-14T17:57:50.125879Z",
    "company_direction": {
      "id": 2,
      "direction": "Адмiнiстрацiя, керівництво середньої ланки"
    }
  }
]
```

</details>

<details> <summary>JSON POST Request</summary>

```json

{
  "id": 1,
  "company_name": "Test Company 2",
  "company_short_description": "Test description 2",
  "vacancy_name": "Test vacancy name 2",
  "vacancy_description": "Test vacancy description 2",
  "vacancy_requirements": "Test 2",
  "vacancy_working_conditions": "Test 2",
  "vacancy_salary": "1000-2000$",
  "vacancy_benefits": "Test 2",
  "vacancy_contacts": "Test 2\r\nTest 2\r\nTest 2",
  "company_website": "Test.com 2 \r\nTest.org 2\r\nTest.ua 2",
  "company_direction": 2
}
```

</details>

--------------------

### Resumes API

ALLOW:

- GET
- POST

<details><summary>Fields:</summary>

- id (primary key)
- students_pib (max length = 90) *
- students_phone_number (max length = 50) *
- students_email (max length = 90) *
- students_direction (foreign key to Directions) *
- students_work_time (foreign key(s) to Work Time) (minimal 1)*
- students_resume_file (file)
- students_resume_link (text area)
- students_social_networks (text area)

</details>

<details><summary>JSON GET Request</summary>

```json
[
  {
    "id": 1,
    "students_pib": "Test 1",
    "students_phone_number": "+380999999999",
    "students_email": "test.test@test.test",
    "students_resume_file": null,
    "students_resume_link": "test.test",
    "students_social_networks": null,
    "resume_date_added": "2021-10-14T17:18:00.261427Z",
    "students_direction": {
      "id": 17,
      "direction": "Робочі спеціальності, виробництво"
    },
    "students_work_time": [
      1,
      2
    ]
  },
  {
    "id": 2,
    "students_pib": "test",
    "students_phone_number": "test",
    "students_email": "test",
    "students_resume_file": null,
    "students_resume_link": "test",
    "students_social_networks": null,
    "resume_date_added": "2021-10-14T17:19:19.866697Z",
    "students_direction": {
      "id": 3,
      "direction": "Будівництво, архітектура"
    },
    "students_work_time": [
      1,
      2,
      3
    ]
  }
]
```

</details>

<details><summary>JSON POST Request</summary>

```json
{
  "students_pib": "test",
  "students_phone_number": "test",
  "students_email": "test",
  "students_resume_file": null,
  "students_resume_link": "test",
  "students_social_networks": null,
  "students_direction": 2,
  "students_work_time": [
    1,
    2,
    3
  ]
}
```

</details>

### Amount of Vacancies and Resumes API

ALLOW: 
- GET

<details><summary>Fields:</summary>

- vacancy_amount
- resume_amount

</details>

<details><summary>JSON GET Request</summary>

```json
{
    "vacancy_amount": 2,
    "resume_amount": 3
}
```

</details>