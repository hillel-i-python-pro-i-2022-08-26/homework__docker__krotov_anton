def test(one):
    print("Запуск функции ...")
    step = 3
    cur = 0
    for i in range(one):
        cur += step
        print("Это первое выполнение функции " + str(i) + " шаг")
        print("На данный момент позиция находится на первой позиции " + str(cur) + " Место")
        yield cur


t = test(10)
print(t)
print(next(t))
print(next(t))
print(next(t))
