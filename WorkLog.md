# WorkLog / UFO 项目运行排障记录

| 日期       | 2025-11-20 → 2025-11-24 |
|------------|-------------------------|
| 记录人     | 梁                      |
| 仓库       | resume-submission-system |

---

## 2025-11-20
- 阅读 UFO 目录下 `README.md`，确认运行命令：  
  `python -m ufo`
- 当前环境 Python 3.8，**不满足**项目要求 ≥3.10。
- 首次安装依赖报错：
  - `matplotlib==3.10.7` 在 PyPI **不存在**
  - Anaconda 自带科学包与 UFO 依赖 **版本冲突**

---

## 2025-11-24
### 1. 安装独立 Python 3.11.6
- 官方下载页：https://www.python.org/downloads/release/python-31110/  
- 安装路径：  
  `C:\Users\liang\AppData\Local\Programs\Python\Python311\python.exe`

### 2. 新建虚拟环境（PowerShell）
```powershell
cd D:\Downloads\resume-submission-system\UFO
&C:\Users\liang\AppData\Local\Programs\Python\Python311\python.exe -m venv venv
.\venv\Scripts\activate
# 提示符变为 (venv) PS D:\…\UFO&gt;