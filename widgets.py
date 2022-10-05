from pygame.surface import Surface

class UIElement:
    def __init__(self, parent, area):
        self.surface = Surface((area.width, area.height))
        self.parent = parent
        self.area = area # relative to parent!
        self.children = []

    def on_click(self, pos):
        """
        Fired when the user clicks the mouse button,
        and the cursor is inside the area of the widget.
        The pos argument is the cursors position,
        translated to the widgets cordinate-system.
        """
        for child in self.children:
            if child.area.collidepoint(pos):
                pos = pos - child.area.topleft
                child.on_click(pos)
                break

    def on_hover(self, pos):
        """
        Fired constantly while the cursor is inside the 
        area of the widget.
        The pos argument is the cursors position,
        translated to the widgets cordinate-system.
        """
        for child in self.children:
            print(pos)
            print(child.area)
            print(child.area.collidepoint(pos))
            if child.area.collidepoint(pos):
                print("runs")
                pos = pos - child.area.topleft
                print(pos)
                child.on_hover(pos)
                break

    def re_draw(self):
        """
        Should call self.parent.re_draw() at the end of 
        the function's body.
        Otherwise it isn't called automaticly, and should
        be called manually instead on demand.
        """
        for child in self.children:
            self.surface.blit(child.surface, child.area)
        self.parent.re_draw()

    def update(self, delta):
        """
        Called on every frame step.
        """
        pass

    def _update(self, delta):
        for child in self.children:
            child._update(delta)
        self.update(delta)


class UIRoot(UIElement):
    def re_draw(self):
        for child in self.children:
            self.surface.blit(child.surface, child.area)

