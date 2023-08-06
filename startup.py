import home
import appsList
import c
while True:
    try:
        home.homePrint()
    except NotImplementedError:
        print("dettected button closing home")
        c.refresh()
        break
        #appsList.list()
    except:
        print("Error")