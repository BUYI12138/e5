import tkinter as tk
from tkinter import messagebox
import time

# 创建主窗口
root = tk.Tk()
root.title("专注时钟")

# 设置初始时间（以秒为单位）
initial_time = 25 * 60  # 25分钟

# 创建倒计时函数
def countdown():
    global initial_time
    if initial_time > 0:
        minutes, seconds = divmod(initial_time, 60)
        time_str = f"{minutes:02}:{seconds:02}"
        label.config(text=time_str)
        initial_time -= 1
        label.after(1000, countdown)  # 每1000毫秒（1秒）调用一次countdown
    else:
        messagebox.showinfo("时间到", "专注时间已结束！")
        root.destroy()

# 创建开始按钮
start_button = tk.Button(root, text="开始专注", command=countdown)
start_button.pack()

# 创建显示时间的标签
label = tk.Label(root, text="00:00", font=("Helvetica", 48))
label.pack()

# 运行主循环
root.mainloop()
