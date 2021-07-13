import win32com.client  as client

excel = client.Dispatch('Excel.Application')
excel.visible =True
_=input("Press Enter to quit:")

excel.Application.quit()