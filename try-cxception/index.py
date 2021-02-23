
import sys
import traceback
a = [1, 5, 8, 6, 5, 5, 8, 4]


class myError(Exception):
    pass


try:
    b = [it for it in a if 5 % it == 0]
    raise myError('errorrrrrrrrrrrrr')
except ZeroDivisionError:
    print("0不能為除數")
except Exception as e:
    error_class = e.__class__.__name__  # 取得錯誤類型
    detail = e.args[0]  # 取得詳細內容
    cl, exc, tb = sys.exc_info()  # 取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1]  # 取得Call Stack的最後一筆資料
    fileName = lastCallStack[0]  # 取得發生的檔案名稱
    lineNum = lastCallStack[1]  # 取得發生的行號
    funcName = lastCallStack[2]  # 取得發生的函數名稱
    errMsg = f"File \"{fileName}\", line {lineNum}, in {funcName}: [{error_class}] {detail}"
    print(errMsg)
else:
    print('沒有異常')
finally:
    pass
# print('finish')
