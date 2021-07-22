Set oShell = CreateObject ("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c run1.bat"
oShell.Run strArgs, 0, false