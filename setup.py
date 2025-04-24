from setuptools import setup, find_packages
import LauncherTemplate
setup(
    name="mypatches",
    version="0.1",
    packages=find_packages(),
    install_requires=["matplotlib"],  # 填写依赖项（如 "numpy>=1.20"）
)