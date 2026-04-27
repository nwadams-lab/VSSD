#!/usr/bin/env python
# coding: utf-8

# In[16]:


import platform
plat = platform.system()


# In[17]:


#If user is using a Windows os, this gives info on system version and if its up to date
def Scanner(plat):
    if plat == "Windows":
        current_ver = platform.version()
        latest_stab_ver = "10.0.26200"
        if current_ver < latest_stab_ver:
            return "Windows version not up to date. Recommended to update your system."
        elif current_ver == latest_stab_ver:
            return "Windows version is up to date!"
        else:
            return "Windows version exceeds common available version."
#If user is using a Linux os, this gives info on system version and if its up to date
    if plat == "Linux":
        current_ver = platform.release()
        latest_stab_ver = "6.19.12"
        if current_ver < latest_stab_ver:
            return "Linux version not up to date. Recommended to update your system."
        elif current_ver == latest_stab_ver:
            return "Linux version is up to date!"
        else:
            return "Linux version exceeds common available version."
#Work in progress cannot test
#If user is using a Mac os, this gives info on system version and if its up to date
    if plat == "Darwin":
        current_ver = platform.release()
        lastest_stab_ver = "26.4.1"
        if current_ver < latest_stab_ver:
            return "Mac version not up to date. Recommended to update your system."
        elif current_ver == latest_stab_ver:
            return "Mac version is up to date!"
        else:
            return "Mac version exceeds common available version."
#Work in progress cannot test


# In[ ]:




