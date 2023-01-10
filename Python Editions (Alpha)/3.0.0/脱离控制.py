print('脱离控制Python版 v3.0.0')
import time
time.sleep(1)
import os
os.system('cls')

os.system('color 9')
print('□■■■■■■□■■■■■■■□■■■■■■□□□■■■■■■□')
print('□■■□□■■□■■□□□■■■■■□□■■□□□■■□□■■■')
print('■■□□□□□□■■□□□■■■■□□□□■■□■■□□□□■■')
print('■■□□■■■■■■■■■■□■■□□□□■■□■■□□□□□□')
print('■■□□□□■■■■□□□■■■■□□□□■■□■■□□□□□□')
print('□■■□□■■■■■□□□■■■■■□□■■□□■■□□□□■■')
print('□■■■■■■■■■□□□■■□■■■■■■□□□■■□□■■□')
print('□□□■□□□□□□□□□□□□□□□□□□□□□■■■■■■□')
print('脱离控制Python版 v3.0.0')
print('2023年第一版！')
print('Copyright TCTFStudio 2021-2023')
import time
time.sleep(1.5)
import os
os.system('cls')

os.system('color a')
print("■■■■■■■■□□■■■■□□■■■■■■■■□■■■■■■■")
print("■■■■■■■■□■■■■■■□■■■■■■■■□■■■■■■■")
print("□□□■■□□□■■□□□□■■□□□■■□□□□■■□□□□□")
print("□□□■■□□□■■□□□□□□□□□■■□□□□■■■■■■■")
print("□□□■■□□□■■□□□□□□□□□■■□□□□■■■■■■■")
print("□□□■■□□□■■□□□□■■□□□■■□□□□■■□□□□□")
print("□□□■■□□□□■■■■■■□□□□■■□□□□■■□□□□□")
print("□□□■■□□□□□■■■■□□□□□■■□□□□■■□□□□□")
print('\000')
print('2023年第一版！')
print('Copyright TCTFStudio 2021-2023')
import time
time.sleep(1.5)


var = 1
while (var == 1):#无限循环
    import os
    os.system('cls')
    import os
    os.system('color 0f')
    print('脱离控制Python版 v3.0.0')
    print("按下enter以脱离控制，a + enter 关于,e + enter 退出")
    choice = input('请输入')
    
    if (choice == 'a'):
        print('TCTF Studio')
        print('网址 tctf.code.blog tctf.mysxl.cn')
        print('email tctf2021@outlook.com')
        print('enter来返回')
        input()
    elif(choice):
        print('再见 \n --TCTF Studio')
        exit()
    else:
        import subprocess
        p = subprocess.Popen('taskkill /f /im StudentMain.exe', shell=True)
        print(p.returncode)
        p.wait()
        print(p.returncode)
        print('返回为0或128则为成功，其他值则失败')
        print('感谢使用  \n --TCTF Studio')
        import time
        time.sleep(2)
