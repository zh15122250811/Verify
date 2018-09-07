import random
from PIL import ImageDraw, Image, ImageFont
from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from django.urls import reverse




# 获取验证码
def get_verify(request):
    # 画板 Img    画笔

    # 创建一个画板
    size = (150, 50)  # (宽,高)
    color = getRandomColor()  # (红,绿,蓝)
    image = Image.new("RGB", size, color)

    # 创建一个画笔,画笔绑定在画板上
    imageDraw = ImageDraw.Draw(image,"RGB")
    # 设置一个字体样式
    imagefont = ImageFont.truetype('/home/zh/django1804/day07/static/fonts/ADOBEARABIC-BOLD.OTF',40)

    charSours = "1234567789asdfghasdfghjzxcvbnasdfghjkQWERTYUIOPLKJHGFDSAZXCVBNM"

    verifyCode = ""
    # 随机生成4个不同字母,并且设置不同颜色
    for i in range(4):
        char = random.choice(charSours)
        verifyCode += char

        # 画图
        # 设置字体样式,用font 属性  fill
        # imageDraw.text((20, 10), 'Mabc', font=imagefont)
        imageDraw.text((20+30*i, 5), char, font=imagefont,fill=getRandomColor())

    # 用session记录验证码,方便对比
    request.session["verifyCode"] = verifyCode

    # 加些点--模糊
    for i in range(500):
        # 设置一个随机位置和随机色
        imageDraw.point(getRandomPosi(),fill=getRandomColor())


    # 读写模块,将图片放进缓冲区
    import io
    buf = io.BytesIO()
    image.save(buf,'png')
    # 响应给客户端
    return HttpResponse(buf.getvalue(),'image/png')


# 获得一个随机颜色
def getRandomColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red,green,blue)

# 获得一个随机位置
def getRandomPosi():
    x = random.randint(0,150)
    y = random.randint(0,50)
    return (x,y)




# 模拟登录--要求输入和验证 验证码
def logUser(request):
    return render(request,'loginUser.html')

# 验证码
def dologin(request):
    # 获取输入的验证码
    verify = request.POST.get("verify")

    # 验证
    # 从session取出验证码
    verifyCode = request.session.get('verifyCode')
    if verify == verifyCode:
        return HttpResponse("验证成功")
    else:
        # 重定向到验证页面
        return redirect(reverse("app:logUser"))