# -*- mode: python ; coding: utf-8 -*-
# 同一份代码打两个程序，放在同一个文件夹里共用依赖：
#   msub.exe          窗口版：没有黑色窗口，托盘图标 + 独立窗口（日常使用）
#   msub-console.exe  控制台版：带黑色窗口，能看到输出，用于排错和自检
from PyInstaller.utils.hooks import collect_all

seg_datas, seg_binaries, seg_hidden = collect_all("segno")
hiddenimports = seg_hidden + ["pystray", "pystray._base", "pystray._win32"]

a = Analysis(
    ["build_entry.py"],
    pathex=["."],
    binaries=seg_binaries,
    datas=seg_datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    runtime_hooks=[],
    excludes=["tkinter"],
    noarchive=False,
)
pyz = PYZ(a.pure)

common = dict(exclude_binaries=True, debug=False, strip=False, upx=False, icon="msub.ico")
exe_gui = EXE(pyz, a.scripts, [], name="msub", console=False, **common)
exe_con = EXE(pyz, a.scripts, [], name="msub-console", console=True, **common)

coll = COLLECT(exe_gui, exe_con, a.binaries, a.datas, strip=False, upx=False, name="msub")
