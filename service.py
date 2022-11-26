# pip install tabulate
# Реализует возможности табличного отображения данных

from tabulate import tabulate

columns = ['programming language', 'type', 'year']

tuples_list = [('Python', 'interpreted', '1991'),
               ('JAVA', 'compiled', '1995'),
               ('С', 'compiled', '1972')]
print(tabulate(tuples_list, headers=columns))
# programming language    type           year
# ----------------------  -----------  ------
# Python                  interpreted    1991
# JAVA                    compiled       1995
# С                       compiled       1972

print(tabulate(tuples_list, headers='firstrow'))  # headers='firstrow': заголовок - первая строка
# Python    interpreted      1991
# --------  -------------  ------
# JAVA      compiled         1995
# С         compiled         1972

dicts_list = [{'programming language': 'Python',
               'type': 'interpreted',
               'year': '1991'},
              {'programming language': 'JAVA',
               'type': 'compiled',
               'year': '1995'},
              {'programming language': 'С',
               'type': 'compiled',
               'year': '1972'}]
print(tabulate(dicts_list, headers='keys'))
# programming language    type           year
# ----------------------  -----------  ------
# Python                  interpreted    1991
# JAVA                    compiled       1995
# С                       compiled       1972

# Стилизация таблиц

# grid-формат
print(tabulate(dicts_list, headers='keys', tablefmt="grid"))
# +------------------------+-------------+--------+
# | programming language   | type        |   year |
# +========================+=============+========+
# | Python                 | interpreted |   1991 |
# +------------------------+-------------+--------+
# | JAVA                   | compiled    |   1995 |
# +------------------------+-------------+--------+
# | С                      | compiled    |   1972 |
# +------------------------+-------------+--------+
# markdown-формат
print(tabulate(dicts_list, headers='keys', tablefmt="pipe"))
# +------------------------+-------------+--------+
# | programming language   | type        |   year |
# |:-----------------------|:------------|-------:|
# | Python                 | interpreted |   1991 |
# | JAVA                   | compiled    |   1995 |
# | С                      | compiled    |   1972 |
# html-формат
print(tabulate(dicts_list, headers='keys', tablefmt="html"))
# <table>
# <thead>
# <tr><th>programming language  </th><th>type       </th><th style="text-align: right;">  year</th></tr>
# </thead>
# <tbody>
# <tr><td>Python                </td><td>interpreted</td><td style="text-align: right;">  1991</td></tr>
# <tr><td>JAVA                  </td><td>compiled   </td><td style="text-align: right;">  1995</td></tr>
# <tr><td>С                     </td><td>compiled   </td><td style="text-align: right;">  1972</td></tr>
# </tbody>
# </table>

# Выравнивание столбцов
print(tabulate(dicts_list, headers='keys', tablefmt="pipe", stralign="center"))
# |  programming language  |    type     |   year |
# |:----------------------:|:-----------:|-------:|
# |         Python         | interpreted |   1991 |
# |          JAVA          |  compiled   |   1995 |
# |           С            |  compiled   |   1972 |

