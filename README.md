no projeto de automação de envio de email para meu email, é necessário o download da biblioteca pyautogui, no código é utilizado a tecla "tab", mas pode ser substituida para o uso de mouse utilizando o código de localização de mouse que coloque junto ao código de envio de email
fazendo a substituiçao de "tab" pelo código:

pyautogui.moveTo("x aqui","y aqui")

pyautogui.mouseDown()

pyautogui.mouseUp()
