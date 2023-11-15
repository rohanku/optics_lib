import sys, os

sys.path.append("C:\\Program Files\\Lumerical\\v212\\api\\python\\")  # Windows
sys.path.append("/opt/lumerical/v221/api/python")  # Linux

lumapi = None

try:
    import lumapi
except Exception as e:
    print(
        "Unable to import lumapi, make sure the appropriate path has been added to PYTHONPATH."
    )
    print("Windows default: C:\\Program Files\\Lumerical\\v212\\api\\python\\")
    print("Linux default: /opt/lumerical/v221/api/python/lumapi.py")
