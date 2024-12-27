#Входные данные:
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

a = "В команде Мастера кода участников: %s !" %team1_num
b = "Итого сегодня в команда участников: %s и %s" %(team1_num, team2_num)
c = "Команда Волшебники данных решила задач: {}!".format(score_2)
d = "Волшебники данных решили задачи за {} с!".format(team1_time)
e = f'Команды решили {score_1} и {score_2} задач.'
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
    challenge_result = result
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
    challenge_result = result
else:
    result = 'Ничья!'
    challenge_result = result
k = f"Результат битвы: {challenge_result}"
#tasks_total = score_1 + score_2
#time_avg = round(((team1_time + team2_time) / tasks_total), 1)
l = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."

print(f'{a}\n {b}\n {c}\n {d}\n {e}\n {k}\n {l}\n')
