import home
import appsList
import c
while True:
    try:
        home.homePrint()

    except NotImplementedError:
        c.refresh()
        appsList.appList()
        break

    except KeyboardInterrupt:
        c.refresh()
        print("closing")
        break

    except:
        print("Error")