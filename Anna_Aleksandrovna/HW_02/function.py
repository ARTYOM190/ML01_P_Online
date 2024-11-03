def function(x):
    return -26 * x ** 2 + 25 * x - 9

def derivative(x):
    return -52 * x + 25

def find_extremes(start, end, step):
    min_value = float('inf')
    max_value = float('-inf')
    min_x = start
    max_x = start

    x = start
    while x <= end:
        y = function(x)
        
        # Проверяем наименьшее значение
        if y < min_value:
            min_value = y
            min_x = x
        
        # Проверяем наибольшее значение
        if y > max_value:
            max_value = y
            max_x = x

        x += step

    return (min_x, min_value), (max_x, max_value)

def main():
    start = -5
    end = 5
    step = 0.1

    min_point, max_point = find_extremes(start, end, step)

    print(f"Наименьшее значение функции: y = {min_point[1]:.2f} при x = {min_point[0]:.2f}")
    print(f"Наибольшее значение функции: y = {max_point[1]:.2f} при x = {max_point[0]:.2f}")

    # Находим особую точку (где производная равна нулю)
    special_x = 25 / 52  # Значение x, при котором производная равна нулю
    if start <= special_x <= end:
        special_y = function(special_x)
        print(f"Особая точка (максимум): x = {special_x:.2f}, y = {special_y:.2f}")
    else:
        print("Особая точка находится вне заданного отрезка.")

if __name__ == "__main__":
    main()