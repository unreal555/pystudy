# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['xuexiqiangguo.py'],
             pathex=['D:\\PyCharm2018.3.3\\pystudy'],
             binaries=[],
             datas=[('./libiconv-2.dll','.'),('./libzbar-32.dll','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='xuexiqiangguo',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
