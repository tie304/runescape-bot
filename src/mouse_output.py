from pynput.mouse import Button, Controller


class MouseOutput:
    def __init__(self):
        self.mouse = Controller()

    def set_mouse_position(self, x, y):
        self.mouse.position = (x, y)

    def click(self, button):
        assert button == "Button.left" or button == "Button.right", "needs to be 'left' or 'right'"
        if button == "Button.left":
            self.mouse.press(Button.left)
            self.mouse.release(Button.left)
        else:
            self.mouse.press(Button.right)
            self.mouse.release(Button.right)

