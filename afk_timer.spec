# sound_timer.spec

block_cipher = None

a = Analysis(
    ['afk_timer.py'],
    pathex=[],
    binaries=[],
    datas=[('sound1.mp3', '.'), ('sound2.mp3', '.'), ('sound3.mp3', '.'), ('sound4.mp3', '.'), ('app_icon.ico', '.')],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='bg_afk_timer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='app_icon.ico'
)
