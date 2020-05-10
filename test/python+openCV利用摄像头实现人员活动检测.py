import cv2
import time

# 定义摄像头对象，其参数0表示第一个摄像头
camera = cv2.VideoCapture(0)
# 测试用,查看视频size
width = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = width, height
# 打印一下分辨率
print(repr(size))
# 设置一下帧数和前背景
fps = 5
pre_frame = None

while True:
    # 读取视频流
    ret, frame = camera.read()
    if not ret:
        print("打开摄像头失败")
    break
    end = time.time()

    cv2.imshow("capture", frame)

    # 运动检测部分,看看是不是5FPS
    seconds = end - start
    if seconds < 1.0 / fps:
        time.sleep(1.0 / fps - seconds)
    gray_pic = cv2.resize(gray_pic, (480, 480))
    # 用高斯滤波进行模糊处理
    gray_pic = cv2.GaussianBlur(gray_pic, (21, 21), 0)

    # 如果没有背景图像就将当前帧当作背景图片
    if pre_frame is None:
        pre_frame = gray_pic
    else:
        # absdiff把两幅图的差的绝对值输出到另一幅图上面来
        img_delta = cv2.absdiff(pre_frame, gray_pic)
    # threshold阈值函数(原图像应该是灰度图,对像素值进行分类的阈值,当像素值高于（有时是小于）阈值时应该被赋予的新的像素值,阈值方法)
    thresh = cv2.threshold(img_delta, 30, 255, cv2.THRESH_BINARY)[1]
    # 用一下腐蚀与膨胀
    thresh = cv2.dilate(thresh, None, iterations=2)
    # findContours检测物体轮廓(寻找轮廓的图像,轮廓的检索模式,轮廓的近似办法)
    image, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        # 设置敏感度
        # contourArea计算轮廓面积
        if cv2.contourArea(c) < 1000:
            continue
        else:
            print("有人员活动！！！")
        # 保存图像
        TI = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        cv2.imwrite("D:\\PYthon\\first_j\\" + "JC" + TI + '.jpg', frame)
        break
    pre_frame = gray_pic

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release()释放摄像头
camera.release()
# destroyAllWindows()关闭所有图像窗口
cv2.destroyAllWindows()
