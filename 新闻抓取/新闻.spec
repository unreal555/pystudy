# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['新闻.py'],
             pathex=['D:\\PyCharm2019.3.1\\pystudy\\新闻抓取'],
             binaries=[],
             datas=[('./my_csv_tools.py','.'),('./mttools.py','.'),('./my_logger.py','.')],
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
          name='新闻',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
