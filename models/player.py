class Player:
    def __init__(self, name, steam_id, x=0, y=0, z=0, pitch=0, yaw=0):
        self.name = name
        self.steam_id = steam_id
        self.x = x
        self.y = y
        self.z = z
        self.pitch = pitch
        self.yaw = yaw # Probably only need this if top-down

        self.health = 100
        self.armour = 0
        self.dead = False
        self.is_shooting = False
        self.current_weapon = None

        self.kills = 0
        self.deaths = 0
        self.assists = 0

        ## UI-related state
        self.is_selected = False
        self.is_hovered = False

    