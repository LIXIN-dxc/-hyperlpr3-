import tkinter as tk
from tkinter import messagebox  # 关键：单独导入messagebox
from datetime import datetime
from test1 import main_1


class SimpleLicensePlateApp:
    def __init__(self, root):
        self.root = root
        self.root.title("车牌识别")
        self.root.geometry("300x200")

        # 存储车牌数据的字典
        self.plate_data = {}

        # 创建界面
        self.label = tk.Label(root, text="车牌识别系统", font=("Arial", 14))
        self.label.pack(pady=10)

        self.recognize_btn = tk.Button(root, text="开始识别", command=self.start_recognition, width=15)
        self.recognize_btn.pack(pady=5)

        self.result_label = tk.Label(root, text="识别结果: 无", font=("Arial", 10))
        self.result_label.pack(pady=5)

        self.show_data_btn = tk.Button(root, text="显示所有车牌", command=self.show_all_data, width=15)
        self.show_data_btn.pack(pady=5)

    def start_recognition(self):
        """模拟车牌识别过程"""
        # 这里应该是调用您的车牌识别代码
        # 识别结果字符串（示例）

        recognized_plate = main_1()  # 替换为您的识别结果

        # 保存到字典
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        plate_id = f"plate_{len(self.plate_data) + 1:03d}"

        self.plate_data[plate_id] = {
            "number": recognized_plate,
            "timestamp": timestamp
        }

        # 更新显示
        self.result_label.config(text=f"识别结果: {recognized_plate}")

        # 修复：使用正确导入的messagebox
        messagebox.showinfo("识别成功", f"车牌 {recognized_plate} 已保存")

    def show_all_data(self):
        """显示所有已识别的车牌数据"""
        if not self.plate_data:
            messagebox.showinfo("数据", "暂无车牌数据")
            return

        # 创建新窗口显示数据
        data_window = tk.Toplevel(self.root)
        data_window.title("所有车牌数据")
        data_window.geometry("300x400")

        text_widget = tk.Text(data_window, height=20, width=35)
        text_widget.pack(padx=10, pady=10)

        # 添加滚动条
        scrollbar = tk.Scrollbar(data_window, command=text_widget.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        text_widget.config(yscrollcommand=scrollbar.set)

        # 插入数据
        for plate_id, info in self.plate_data.items():
            text_widget.insert(tk.END,
                               f"ID: {plate_id}\n"
                               f"车牌: {info['number']}\n"
                               f"时间: {info['timestamp']}\n"
                               f"{'-' * 30}\n")


def main():
    root = tk.Tk()
    app = SimpleLicensePlateApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()