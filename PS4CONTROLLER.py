from pyPS4Controller.controller import Controller


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
       print("Hello world")

    def on_x_release(self):
       print("Goodbye world")

    def on_L3_up(self, value):
        #print("L3 :" + str(value))
        pass
    

class PS4():
    def connect(self):
    # any code you want to run during initial connection with the controller
        self.connected = True

    def disconnect(self):
    # any code you want to run during loss of connection with the controller or keyboard interrupt
        self.connected = False

    def start(self):
        self.controller.listen(timeout=15,on_connect=self.connect, on_disconnect=self.disconnect)

    def __init__(self):
        self.connected = False
        self.controller = MyController(interface="/dev/input/js1", connecting_using_ds4drv=False)
        # you can start listening before controller is paired, as long as you pair it within the timeout window
        


#con = PS4()