import numpy as np
import requests

start=int(input("start of page?"))
end=int(input("End of page?"))+1
gap=int(input("The gap between pages?"))
path=input("enter file path eg D:\pictures\page")
pages = np.arange(start, end,gap)
for i in pages:
    
    name= "D:\pictures\page"+str(i)+".jpg"
    page="https://images.lib.cam.ac.uk/content/images/PR-ADV-B-00039-00001-000-0000" + str(i) + ".jpg"
    print(page)
    print(name)
    myfile = requests.get(page)
    open(name, 'wb').write(myfile.content)
