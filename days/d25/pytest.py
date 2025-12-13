import pygame
from math import sqrt


class Node:

    def __init__(self, name ,pos, connections):

        self.screen:pygame.Surface = pygame.display.get_surface()
        self.name:str = name
        self.pos = pygame.Vector2(pos)
        self.connections:list[str] = connections
        self.selected = False
        self.radius = 10
        self.color = 0x33AA33

    def is_mouse_coll(self, mouse_pos):
        return self.pos.distance_squared_to(mouse_pos) <= self.radius**2

    def get_selected(self, mouse_pos):

        if self.is_mouse_coll(mouse_pos):
            self.selected = True
            return True

    def update(self, movt):
        
        if self.selected:
            self.pos += movt

    def draw(self):

        pygame.draw.circle(self.screen, self.color, self.pos, self.radius)
        for comp in self.connections:
            pos = nodes[comp].pos
            pygame.draw.line(self.screen, 0x3333AA, self.pos, pos, 3)
        # mouse_pos = pygame.mouse.get_pos()
        # if self.is_mouse_coll(mouse_pos):
        text = font.render(self.name, True, 0xFFFFFFFF)
        self.screen.blit(text, self.pos+(-text.get_height(), -text.get_width()/2))


pygame.init()
screen = pygame.display.set_mode((600, 600))
font = pygame.Font(None, 30)

# components = {'jqt': ['rhn', 'xhk', 'nvd'], 'rsh': ['frs', 'pzl', 'lsr'], 'xhk': ['hfx'], 'cmg': ['qnr', 'nvd', 'lhk', 'bvb'], 'rhn': ['xhk', 'bvb', 'hfx'], 'bvb': ['xhk', 'hfx'], 'pzl': ['lsr', 'hfx', 'nvd'], 'qnr': ['nvd'], 'ntq': ['jqt', 'hfx', 'bvb', 'xhk'], 'nvd': ['lhk'], 'lsr': ['lhk'], 'rzs': ['qnr', 'cmg', 'lsr', 'rsh'], 'frs': ['qnr', 'lhk', 'lsr']}
components = {'jqt': ['rhn', 'xhk', 'nvd', 'xhk', 'rhn', 'ntq', 'nvd'], 'rsh': ['frs', 'pzl', 'lsr', 'pzl', 'lsr', 'rzs', 'frs'], 'xhk': ['hfx', 'jqt', 'rhn', 'bvb', 'ntq'], 'cmg': ['qnr', 'nvd', 'lhk', 'bvb', 'bvb', 'qnr', 'nvd', 'rzs'], 'rhn': ['xhk', 'bvb', 'hfx', 'jqt', 'bvb'], 'bvb': ['xhk', 'hfx', 'cmg', 'rhn', 'ntq'], 'pzl': ['lsr', 'hfx', 'nvd', 'rsh', 'nvd', 'lsr'], 'qnr': ['nvd', 'cmg', 'nvd', 'rzs', 'frs'], 'ntq': ['jqt', 'hfx', 'bvb', 'xhk'], 'nvd': ['lhk', 'jqt', 'cmg', 'pzl', 'qnr'], 'lsr': ['lhk', 'rsh', 'pzl', 'rzs', 'frs'], 'rzs': ['qnr', 'cmg', 'lsr', 'rsh'], 'frs': ['qnr', 'lhk', 'lsr', 'rsh'], 'hfx': ['xhk', 'rhn', 'bvb', 'pzl', 'ntq'], 'lhk': ['cmg', 'nvd', 'lsr', 'frs']}


nodes:dict[str, Node] = {}
for i, (name, comps) in enumerate(components.items()):

    y, x = divmod(i, 4)
    node = Node(name, (x*50+100, y*50+100), comps)
    nodes[name] = node

while True:

    pygame.display.flip()

    mouse_movt = [0, 0]

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for node in nodes.values():
                if node.get_selected(event.pos):
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            for node in nodes.values():
                node.selected = False
        elif event.type == pygame.MOUSEMOTION:
            mouse_movt[0] += event.rel[0]
            mouse_movt[1] += event.rel[1]

    for node in nodes.values():
        node.update(mouse_movt)
    screen.fill(0x0)
    for node in nodes.values():
        node.draw()
        
