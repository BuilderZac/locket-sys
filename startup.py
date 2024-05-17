import home
import appsList
import c
epd = c.epd()
while True:
    try:
        home.homePrint()
        appsList.appList()

    except NotImplementedError:
        break

    except KeyboardInterrupt:
        epd.sleep()
        print("closing")
        break

#    except:
#        print("Error")
