import home
import appsList
import c
while True:
    try:
        home.homePrint()
        appsList.appList()

    except NotImplementedError:
        break

    except KeyboardInterrupt:
        c.refresh()
        print("closing")
        break

#    except:
#        print("Error")

