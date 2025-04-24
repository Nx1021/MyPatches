import matplotlib.pyplot as plt
import os

def is_ssh_session():
    # 检查SSH相关的环境变量
    if 'SSH_CLIENT' in os.environ or 'SSH_TTY' in os.environ or 'SSH_CONNECTION' in os.environ:
        return True
    return False

def new_plt_show():
    x = plt.show
    def wrapper():
        plt.savefig('_temp_plot.png')
    if is_ssh_session():
        return wrapper
    else:
        return x

plt.show = new_plt_show()