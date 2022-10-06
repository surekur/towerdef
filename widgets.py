from pygame.surface import Surface
from constans import *
import battlefield
from utils import *

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
            if child.area.collidepoint(pos):
                pos = pos - child.area.topleft
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
            print(child)
            self.surface.blit(child.surface, child.area)


class Menu(UIElement):
    def __init__(self, parent, area):
        pass

class ToolBox(UIElement):
    def __init__(self, parent, area, buttonheight):
        super().__init__(parent, area)
        self.buttonheight = buttonheight
        self.elements = []
        self.selected = None
        self.re_draw()

    def re_draw(self):
        self.surface.fill(UIBGCOL)
        for i, element in enumerate(self.elements):
            self.draw_button(element, i == self.selected, 
                    i * self.buttonheight)
        self.parent.re_draw()
    
    def draw_button(self, element, isselected, vpos):
        self.surface.blit(element.icon, (0, vpos))
        shadowcol = 0, 0, 0
        illumination = 120, 120, 120
        if isselected:
            shadowcol = 10, 10, 10
            illumination = 60, 60, 60
        self.surface.fill(shadowcol, (0, vpos+self.buttonheight-2, 
                                    self.area.width, 2))
        self.surface.fill(shadowcol, (self.area.width-2, vpos,
                                    2, self.buttonheight))
        self.surface.fill(illumination, (0, vpos,
                                        self.area.width, 2))
        self.surface.fill(illumination, (0, vpos,
                                        2, self.buttonheight))

    def on_click(self, pos):
        elementindex = int(Vec(pos).y // self.buttonheight)
        if elementindex <= len(self.elements):
            self.elements[elementindex].mechanism(self)
            self.selected = elementindex
            self.re_draw()


class ToolBoxElement:
    def __init__(self, mechanism, icon):
        self.mechanism = mechanism
        self.icon = icon


def select_mgnest(toolbox):
    toolbox.selectedbuilding = battlefield.MGNest

class BuildingPanel(ToolBox):
    def __init__(self, parent, area):
        super().__init__(parent, area, TILESIZE)
        self.selectedbuilding = None
        self.elements = [
                ToolBoxElement(select_mgnest,
                    get_image("data/mg_nest.png")),
                ]
        self.re_draw()
        

