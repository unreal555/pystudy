from point import Point, swap_point

def mid_line(point0, point1):
    if point0.x > point1.x:
        point0, point1 = swap_point(point0, point1)
    dx = point1.x - point0.x
    dy = point1.y - point0.y
    points = []
    if dx == 0:  # 斜率为无穷大，画直竖线
        y_min = min(point0.y, point1.y)
        y_max = max(point0.y, point1.y)
        for y in range(y_min, y_max):
            points.append(Point(point0.x, y))

    elif dy == 0:  # 斜率为零，画水平线
        x_min = min(point0.x, point1.x)
        x_max = max(point0.x, point1.x)
        for x in range(x_min, x_max):
            points.append(Point(x, point0.y))

    x = point0.x
    y = point0.y
    points.append(point0)

    if (dx >= dy) and dy > 0:  # 0<k<=1
        d = (dy * 2) - dx
        while x < point1.x:
            if d > 0:
                d += (dy - dx) * 2
                x += 1
                y += 1
            else:
                d += dy * 2
                x += 1
            points.append(Point(x, y))
    elif (dy > dx) and dy > 0:  # k>1
        d = dy - (dx * 2)
        while y < point1.y:
            if d < 0:
                d += (dy - dx) * 2
                x += 1
                y += 1
            else:
                d += (-dx) * 2
                y += 1
            points.append(Point(x, y))
    elif (dx >= abs(dy)) and dy < 0:  # -1=<k<0
        d = (dy * 2) + dx
        while x < point1.x:
            if d < 0:
                d += (dy + dx) * 2
                x += 1
                y -= 1
            else:
                d += dy * 2
                x += 1
            points.append(Point(x, y))
    elif (abs(dy) > dx) and dy < 0:  # k<-1
        d = dy + (dx * 2)
        while y > point1.y:
            if d > 0:
                d += (dy + dx) * 2
                x += 1
                y -= 1
            else:
                d += (dx) * 2
                y -= 1
            points.append(Point(x, y))

    return points


def dda_line(point0, point1):
    dx = point1.x - point0.x  # x的增量
    dy = point1.y - point0.y  # y的增量
    x = point0.x
    y = point0.y
    if abs(dx) > abs(dy):  # 谁的增量大
        steps = abs(dx)
    else:
        steps = abs(dy)

    xIncrement = float(dx) / float(steps)  # x每步骤增量
    yIncrement = float(dy) / float(steps)  # y的每步增量

    points = [point0]  # 起点
    for k in range(steps):
        x += xIncrement  # x点 + 增量
        y += yIncrement  # y点 + 增量
        points.append(Point(x, y))

    points.append(point1)  # 终点
    return points


def bresenham_line(point0, point1):
    dx = abs(point1.x - point0.x)
    dy = abs(point1.y - point0.y)
    # 根据直线的走势方向，设置变化的单位是正是负
    s1 = 1 if ((point1.x - point0.x) > 0) else -1
    s2 = 1 if ((point1.y - point0.y) > 0) else -1
    # 根据斜率的大小，交换dx和dy，可以理解为变化x轴和y轴使得斜率的绝对值为[0,1]
    boolInterChange = False
    if dy > dx:
        temp = dx
        dx = dy
        dy = temp
        boolInterChange = True
    # 初始误差
    e = 2 * dy - dx
    x = point0.x
    y = point0.y
    points = [point0]  # 起点
    for i in range(0, int(dx + 1)):
        if e >= 0:
            # 此时要选择横纵坐标都不同的点，根据斜率的不同，让变化小的一边变化一个单位
            if boolInterChange:
                x += s1
            else:
                y += s2
            e -= 2 * dx
        # 根据斜率的不同，让变化大的方向改变一单位，保证两边的变化小于等于1单位，让直线更加均匀
        if boolInterChange:
            y += s2
        else:
            x += s1
        e += 2 * dy
        points.append(Point(x, y))
    return points
