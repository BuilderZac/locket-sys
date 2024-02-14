import home
import appsList
import c
while True:
    try:
        home.homePrint()
        c.refresh(0.5)
        appsList.appList()

    except NotImplementedError:
        break

    except KeyboardInterrupt:
        c.refresh()
        print("closing")
        break

    except:
        print("Error")

