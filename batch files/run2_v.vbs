Set oShell = CreateObject ("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c run2.bat"
oShell.Run strArgs, 0, false