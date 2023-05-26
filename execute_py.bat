@echo off
chcp 65001
setlocal enabledelayedexpansion

:menu
REM 获取当前文件夹下的所有子文件夹中的.py文件
set /a count=1
for /d %%I in (*) do (
    pushd "%%I"
    for %%F in (*.py) do (
        REM 读取.py文件中的doc描述
        for /f "tokens=*" %%D in ('type "%%F" ^| findstr /i /c:"\"\"\"') do (
            REM 去除doc描述中的引号和空格
            set "desc=%%D"
            set "desc=!desc:\"=!"
            set "desc=!desc: =!"
            REM 显示文件编号、描述和文件名
            echo !count!. !desc! - %%F
            set /a count+=1
        )
    )
    popd
)

REM 提示用户选择要执行的py文件
set /p choice=请输入要执行的文件编号（输入Q退出）：

if /i "%choice%"=="Q" (
    goto :end
) else (
    REM 执行用户选择的py文件
    set /a exec_count=1
    for /d %%I in (*) do (
        pushd "%%I"
        for %%F in (*.py) do (
            if !exec_count! equ %choice% (
                echo 执行 %%F
                python "%%F"
                if errorlevel 1 (
                    echo 运行失败。
                    pause
                    goto :menu
                ) else (
                    echo 程序运行成功。
                    pause
                    goto :menu
                )
            )
            set /a exec_count+=1
        )
        popd
    )

    REM 用户选择的编号无效
    echo 无效的文件编号。
    pause
    goto :menu
)

:end
endlocal