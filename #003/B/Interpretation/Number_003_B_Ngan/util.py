TableLength = int((TAU * 100) + 1)  # 628 - a full circle.
sintable = [sin(i * 0.01) for i in range(TableLength)]
costable = [cos(i * 0.01) for i in range(TableLength)]


def getFunc(func, val):
    if val < 0:
        val += TAU
    if val >= TAU:
        val -= TAU
    val = min(TAU, max(0, val))  # 6.27
    if func == 'sin':
        return sintable[floor(val * 100)]
    elif func == 'cos':
        return costable[floor(val * 100)]
