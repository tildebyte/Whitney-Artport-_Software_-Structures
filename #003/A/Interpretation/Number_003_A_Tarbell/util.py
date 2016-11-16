def checkBounds(x, y, pad):
    xIncrement = this.width + pad * 2
    yIncrement = this.height + pad * 2
    constrainedX = constrain(x, 0 - pad, this.width + pad)
    constrainedY = constrain(y, 0 - pad, this.height + pad)
    prevx = x
    prevy = y
    if constrainedX != prevx:
        if prevx < 0:
            x += xIncrement
        else:
            x -= xIncrement
    if constrainedY != prevy:
        if prevy < 0:
            y += yIncrement
        else:
            y -= yIncrement
    return x, y
