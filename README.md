# LoriSystemTestTask

#### Python version 3.8.5

#### create env

```python
pyenv install -v 3.8.5
pyenv virtualenv 3.8.3 envname # create env
pyenv local envname# set autodetect local env(activate when cd to folder)
```

#### Install requirements

```python
pip install -r requirements.txt
```

#### Apply migrations
```python
manage.py migrate
```

#### Check test code coverage

```
coverage run --source='.' manage.py test book_store

coverage report
```

#### Coverage report

```text
coverage report
Name                                                     Stmts   Miss  Cover
----------------------------------------------------------------------------
book_rent_store/__init__.py                                  0      0   100%
book_rent_store/asgi.py                                      4      4     0%
book_rent_store/settings.py                                 23      0   100%
book_rent_store/urls.py                                      3      0   100%
book_rent_store/wsgi.py                                      4      4     0%
book_store/__init__.py                                       0      0   100%
book_store/admin.py                                          3      0   100%
book_store/apps.py                                           3      3     0%
book_store/forms.py                                         14      6    57%
book_store/migrations/0001_initial.py                        6      0   100%
book_store/migrations/0002_auto_20200908_2042.py             4      0   100%
book_store/migrations/0003_auto_20200908_2046.py             4      0   100%
book_store/migrations/0004_remove_book_rent_per_day.py       4      0   100%
book_store/migrations/0005_book_image.py                     4      0   100%
book_store/migrations/__init__.py                            0      0   100%
book_store/models.py                                        54      2    96%
book_store/tests/__init__.py                                 0      0   100%
book_store/tests/test_models.py                             73      0   100%
book_store/tests/test_utils.py                               7      0   100%
book_store/tests/test_views.py                              23      0   100%
book_store/urls.py                                           7      0   100%
book_store/utils.py                                         12      0   100%
book_store/views.py                                         30     12    60%
manage.py                                                   12      2    83%
----------------------------------------------------------------------------
TOTAL                                                      294     33    89%
```