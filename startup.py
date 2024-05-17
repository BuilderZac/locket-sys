import home
import appsList
import c
while True:
    try:
        c.refresh()
        home.homePrint()
        appsList.appList()

    except NotImplementedError:
        break

    except KeyboardInterrupt:
        print("closing")
        break

#    except:
#        print("Error")
