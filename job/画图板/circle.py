from point import Point


# 计算圆心 半径
def cal_cir_parm(point0, point1):
    xc = (point0.x - point1.x) / 2 + point1.x
    yc = (point0.y - point1.y) / 2 + point1.y
    r = ((((point0.x - point1.x) / 2) ** 2 + (point0.y - point1.y) / 2 ** 2) ** 0.5).real
    return xc, yc, r


# 使用中点画圆方法时 进行对称点打亮
def mid_whole_point(xc, yc, x, y, points):
    points.append(Point(xc + x, yc + y))
    points.append(Point(xc + y, yc + x))
    points.append(Point(xc - x, yc + y))
    points.append(Point(xc - y, yc + x))
    points.append(Point(xc + x, yc - y))
    points.append(Point(xc + y, yc - x))
    points.append(Point(xc - x, yc - y))
    points.append(Point(xc - y, yc - x))
    return points


# 中点画圆
def mid_circle(point0, point1):
    xc, yc, r = cal_cir_parm(point0, point1)
    points = []
    x = 0.
    y = r
    d = 1 - r
    points = mid_whole_point(xc, yc, x, y, points)
    while x <= y:
        if d < 0:  # 走正右方
            d += 2 * x + 3
            x += 1
        else:  # 走右下方
            d += 2 * (x - y) + 5
            x += 1
            y -= 1
        points = mid_whole_point(xc, yc, x, y, points)
    return points


def bresenham_circle(point0, point1):
    xc, yc, r = cal_cir_parm(point0, point1)
    # 初始化,画第一个点，从水平最右边那个点开始画
    (x, y) = (r, 0)

    """
    从定义来讲就是
    P_k=d1+d2
    d1 = 第1个下一步待选点离圆弧的距离（负数）
    d2 = 第2个下一步待选点离圆弧的距离（正数）
    但是为了提高效率通常使用递推来求P_{k+1}=P_k + 一个数
    """
    P_k = -2 * r + 3
    points = []

    # 迭代的求完1/8圆弧
    while x >= y:
        # 下一步有两个待选点，具体选哪个要看P_k>0 或 <0
        if P_k >= 0:  # 外侧候选点偏离圆弧更远
            P_k_next = P_k - 4 * x + 4 * y + 10
            (x_next, y_next) = (x - 1, y + 1)
        else:  # 内侧候选点偏离圆弧更远
            P_k_next = P_k + 4 * y + 6
            (x_next, y_next) = (x, y + 1)
        # 对称法画其他地方
        points.append(Point(xc + x, yc + y))
        points.append(Point(xc - x, yc + y))
        points.append(Point(xc + x, yc - y))
        points.append(Point(xc - x, yc - y))

        points.append(Point(xc + y, yc + x))
        points.append(Point(xc + y, yc - x))
        points.append(Point(xc - y, yc + x))
        points.append(Point(xc - y, yc - x))
        # 更新坐标和P_k
        (x, y) = (int(x_next), int(y_next))
        P_k = P_k_next
    return points


def bresenham_ellipse(point0, point1):
    xc, yc, _ = cal_cir_parm(point0, point1)
    a = int(abs(point0.x - point1.x) / 2)   # 长半轴
    b = int(abs(point0.y - point1.y) / 2)   # 短半轴
    if a == 0 or b == 0:
        return
    aa = a * a
    bb = b * b
    d1 = bb + aa * (-b + 0.25)

    x = 0
    y = b
    points = [Point(xc + x, yc + y), Point(xc - x, yc + y), Point(xc - x, yc - y), Point(xc + x, yc - y)]

    while bb * (x + 1) < aa * (y - 0.5):
        if d1 <= -0.000001:
            d1 += bb * ((x << 1) + 3)
        else:
            d1 += bb * ((x << 1) + 3) + aa * (2 - (y << 1))
            y -= 1
        x += 1
        points.append(Point(xc + x, yc + y))
        points.append(Point(xc - x, yc + y))
        points.append(Point(xc - x, yc - y))
        points.append(Point(xc + x, yc - y))

    d2 = bb * (0.25 * x) + aa * (1 - (y << 1))
    while y > 0:
        if d2 <= -0.000001:
            x += 1
            d2 += bb * ((x + 1) << 1) + aa * (3 - (y << 1))
        else:
            d2 += aa * (3 - (y << 1))
        y -= 1
        points.append(Point(xc + x, yc + y))
        points.append(Point(xc - x, yc - y))
        points.append(Point(xc - x, yc + y))
        points.append(Point(xc + x, yc - y))
    return points
