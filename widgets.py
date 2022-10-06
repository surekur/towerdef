from pygame.surface import Surface
from constans import *
import battlefield
from utils import *
from pygame import font
from pygame import Rect

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


class TextMenu(UIElement):
    def __init__(self, parent, area):
        super().__init__(parent, area)
        self.elements = []
        self.hovered = None
        self.textsize = 30
        self.bgcol1 = 40,40,40
        self.bgcol2 = 60,60,60
        self.hoveredbg = 60,60,90
        self.font = font.Font(font.get_default_font())

    def re_draw(self):
        self.surface.fill(20,20,20)
        eventh = False
        for i, element in enumerate(self.elements):
            if eventh:
                drawcolor = self.bgcol2
            else:
                drawcolor = self.bgcol1
            eventh = not eventh
            pos = i * self.textsize
            self.surface.fill(drawcolor,
                    Rect(0, pos, self.area.width, self.textsize)
                    )
            textsurf = self.font.render(element.text, True,
                    (255,255,255))
            self.surface.blit(textsurf, (20, pos))

            
    
    def on_hover(self, pos):
        self.hovered = int(Vec(pos).x // self.textsize)
        self.re_draw()


class TextMenuElement:
    def __init__(self, text, payload):
        self.text = text
        self.payload = payload


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
 

def savegame(toolbox):
    toolbox.game.save(toolbox.sql)
    toolbox.game.after_load()
    toolbox.game.parent = toolbox.parent

def loadgame(toolbox):
    pass

class MainPanel(ToolBox):
    def __init__(self, parent, area, game, sql):
        super().__init__(parent, area, TILESIZE)
        self.game = game
        self.sql = sql
        self.elements = [
            ToolBoxElement(savegame,
                get_image("data/savegame.png")),
            ToolBoxElement(loadgame,
                get_image("data/loadgame.png")),
                ]
        self.re_draw()

