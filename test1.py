import cv2
import hyperlpr3 as lpr3

def main_1():
    """
    主函数：启动实时车牌识别
    """
    # 1. 初始化HyperLPR车牌识别器
    catcher = lpr3.LicensePlateCatcher(detect_level=lpr3.DETECT_LEVEL_HIGH)

    # 2. 初始化摄像头
    cap = cv2.VideoCapture(0)

    # 检查摄像头是否成功打开
    if not cap.isOpened():
        print("：无法打开摄像头错误。")
        return

    print("摄像头已打开。按 'q' 键退出程序。")
    #添加计数模块
    count = 0
    count_1 = []
    # 4. 主循环：持续捕获和处理视频帧
    while True:
        # 从摄像头读取一帧图像
        ret, frame = cap.read()

        # 如果读取失败，则跳出循环
        if not ret:
            print("错误：无法从摄像头读取视频帧。")
            break
        # 5. 调用HyperLPR进行车牌识别
        results = catcher(frame)
        # 6. 遍历所有识别到的车牌，并在画面上绘制结果
        for code, confidence, plate_type, box in results:
            # 过滤低置信度的结果
            if confidence > 0.8:
                if count_1 == []:
                    count_1.append(code)
                else:
                    if code in count_1:
                        count += 1
                        print(count)
                    else :
                        count_1 = []
        # 7. 显示处理后的视频帧
        cv2.imshow('Real-time License Plate Recognition (HyperLPR)', frame)
        # 8. 处理退出逻辑
        if count == 4 or (cv2.waitKey(1) & 0xFF == ord('q')) :
            print(count_1)
            print("程序已退出。")
            break


    # 9. 清理工作
    cap.release()
    cv2.destroyAllWindows()
    return count_1

if __name__ == "__main__":
    main_1()