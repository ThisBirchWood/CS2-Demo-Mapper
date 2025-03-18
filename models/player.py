class Player:
    def __init__(self, name, steam_id, x=0, y=0, z=0, pitch=0, yaw=0):
        self.name = name
        self.steam_id = steam_id
        self.x = x
        self.y = y
        self.z = z

        self.pitch = pitch
        self.yaw = yaw # Probably only need this if top-down
        self.dead = False
        self.is_shooting = False

    