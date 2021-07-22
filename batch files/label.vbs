Set oShell = CreateObject ("Wscript.Shell")
oShell.CurrentDirectory = "D:\studies\cse\music recommendation\batch files\"
Dim strArgs
strArgs = "cmd /c music.bat"
oShell.Run strArgs, 0, false