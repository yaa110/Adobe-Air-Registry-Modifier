# switch (rootkey)
root_keys = {
             "HKEY_LOCAL_MACHINE" : _winreg.HKEY_LOCAL_MACHINE,
             "HKEY_CLASSES_ROOT" : _winreg.HKEY_CLASSES_ROOT,
             "HKEY_CURRENT_CONFIG" : _winreg.HKEY_CURRENT_CONFIG,
             "HKEY_CURRENT_USER" : _winreg.HKEY_CURRENT_USER,
             "HKEY_USERS" : _winreg.HKEY_USERS
             }

# switch (action)
actions = {
           "read" : read_key,
           "write" : write_key,
           "writedword" : write_key_dword,
           "delete" : delete_key,
           "check" : check_key,
           }

def read_key():
    try:
        hKey = _winreg.OpenKey(root_keys[rk.upper()], p)
        _value, _type = _winreg.QueryValueEx (hKey, k)
        sys.stdout.write(str(_value))
    except Exception as e:
        sys.stderr.write("Error: " + str(e))

def write_key():
    try:
        key = _winreg.CreateKey(root_keys[rk.upper()], p)
        _winreg.SetValueEx(key, k, 0, _winreg.REG_SZ, v)
        sys.stdout.write('Key has been created.')
    except Exception as e:
        sys.stderr.write("Error: " + str(e))

def write_key_dword():
    try:
        key = _winreg.CreateKey(root_keys[rk.upper()], p)
        _winreg.SetValueEx(key, k, 0, _winreg.REG_DWORD, v)
        sys.stdout.write('DWORD Key has been created.')
    except Exception as e:
        sys.stderr.write("Error: " + str(e))

def delete_key():
    try:
        _winreg.DeleteKey(root_keys[rk.upper()], p)
        sys.stdout.write('Key has been deleted.')
    except Exception as e:
        sys.stderr.write("Error: " + str(e))

def check_key():
    aReg = _winreg.ConnectRegistry(None,root_keys[rk.upper()])
    aKey = _winreg.ConnectRegistry(None,root_keys[rk.upper()])
    try:
        aKey = _winreg.OpenKey(aReg, p, 0)
    except Exception as e:
        sys.stderr.write("Error: " + str(e))
    else:
        sys.stdout.write('exists')
        
    _winreg.CloseKey(aKey)
    _winreg.CloseKey(aReg)

# Get arguments
for i in sys.argv:
    try:
        if i.find("-key") != -1: k = i.split(":")[1]
        elif i.find("-value") != -1: v = i.split(":")[1]
        elif i.find("-path") != -1: p = i.split(":")[1]
        elif i.find("-rootkey") != -1: rk = i.split(":")[1]
        elif i.find("-action") != -1: a = i.split(":")[1]
    except Exception as e:
        sys.stderr.write("Invalid argument: " + str(e))

try:
    actions[a.lower()]()
except Exception as e:
    sys.stderr.write("Invalid action " + a.lower() + ": " + str(e))
