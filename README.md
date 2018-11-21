

# Django UUPortal

## Стек
Используется [Django](https://www.djangoproject.com/) как бекенд проекта, основные зависимости:
- [React](https://facebook.github.io/react/), для создания интерактивных UI интерфейсов
- [django-js-reverse](https://github.com/ierror/django-js-reverse), для создания URL-адресов на JS
- [Bootstrap 4](https://v4-alpha.getbootstrap.com/), для гибкого стиля
- [Webpack](https://webpack.js.org/), для объединения статики
- [Celery](http://www.celeryproject.org/), для фоновых задач
- [WhiteNoise](http://whitenoise.evans.io/en/stable/) with [brotlipy](https://github.com/python-hyper/brotlipy), для эффективного использования статических файлов
- [prospector](https://prospector.landscape.io/en/master/) и [ESLint](https://eslint.org/) с [pre-commit](http://pre-commit.com/) для автоматического обеспечения качества (не заменяет надлежащее тестирование!)

Для непрерывного интегрирования a [CircleCI](https://circleci.com/) конфигурация `.circleci/config.yml`.

Кроме того, для тестирование в Heroku `app.json` и рабочий Django `production.py` настройки, позволяющие легко развертывать ['Deploy to Heroku' button](https://devcenter.heroku.com/articles/heroku-button). Эти плагины Heroku включены в `app.json`:
- PostgreSQL, for DB
- Redis, for Celery
- Sendgrid, for e-mail sending
- Papertrail, для журналов и предупреждений об ошибках платформы (необходимо установить их вручную)

Это хорошая отправная точка для современных веб-проектов Python/JavaScript.

## Running
### Установка
- В корне проекта выполните следующие действия:
- Создайте копию ``uuportal/settings/local.py.example``:  
  `cp uuportal/settings/local.py.example uuportal/settings/local.py`.
- Создайте копию  ``.env.example``:  
  `cp .env.example .env`
- Run the migrations:  
  `python manage.py migrate`

### Дополнительно
- Setup [editorconfig](http://editorconfig.org/), [prospector](https://prospector.landscape.io/en/master/) and [ESLint](http://eslint.org/) in the text editor you will use to develop.

### Запуск проекта
- В терминале:
- `pipenv install --dev`
- `npm install`
- `npm run start`
- В новых вкладках териминала:
- `pipenv shell`
- `python manage.py runserver`

#### Celery
- Для запуска Celery в новом терминале:
- `pipenv shell`
- `python manage.py celery`

### Pycharm 
- При использовании среды Pycharm (начиная с версии 2018.2) возможно создать серверы запуска. 

### Testing
`make test`

Запустите тесты django, используя `--keepdb` и `--parallel`. Можно пройти путь к нужному тестовому модулю в команде make. Например.:

`make test someapp.tests.test_views`

### Добавление новых pypi libs
Запустить `pipenv install LIB_NAME_ON_PYPI` далее `pipenv lock` заблокировать версию в файле Pipfile.lock

## Linting
- Вручную с `prospector` и `npm run lint` в корне проекта.
- Во время разработки с редактором, совместимым с разработчиком и ESLint.

## Pre-commit hooks
- Заупстить `pre-commit install` чтобы включить захват в репозиторий git. Крюк будет запускаться автоматически для каждого коммита.
- Запустить `git commit -m "Your message" -n` пропустить крючок, если вам нужно.
