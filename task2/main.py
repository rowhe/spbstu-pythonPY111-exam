ppl = int(input('Количество участников: '))
words = int(input('Количество слов: '))
# print('Выбывает каждый', words, "-й")

mens_list = list(range(1, ppl + 1))
out = 0

for _ in range(ppl - 1):
    print('Участники', mens_list)
    start_count = out % len(mens_list)
    out = (start_count + words - 1) % len(mens_list)
    print('Начинаем с номера', mens_list[start_count])
    print('Выбывает номер', mens_list[out])
    mens_list.remove(mens_list[out])
    print()

print('Остался номер', mens_list)
