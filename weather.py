import random, math, pygame


'''DAY CYCLE AND WEATHER'''
class Weather:

    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height

        # Time of day: 0.0 to 1.0 (0.25 = noon, 0.75 = midnight)
        self.time = 0.25

        
        self.overlay = pygame.Surface((screen_width, screen_height))

        
        self.snow = []
        for i in range(120):
            
            start_y = random.randint(0, screen_height)
            self.snow.append(self.make_flake(start_y))

    # Returns one snowflake: [x, y, speed, size]
    def make_flake(self, y=-10):
        x     = random.randint(0, self.width)
        speed = random.uniform(1, 3)
        size  = random.randint(2, 4)
        return [x, y, speed, size]

    # Returns a 0.0–1.0 value: 0 = noon (bright), 1 = midnight (dark)
    def get_darkness(self):
        return (1 - math.cos(2 * math.pi * (self.time - 0.25))) / 2

    def update(self):
        
        self.time = (self.time + 0.0000375) % 1.0

        darkness = self.get_darkness()

        #  (80 at noon, 350 at midnight)
        target_count = int(80 + 270 * darkness)

        while len(self.snow) < target_count:
            self.snow.append(self.make_flake())       

        if len(self.snow) > target_count:
            self.snow = self.snow[:target_count]      

 
        for flake in self.snow:
            flake[1] += flake[2]                      
            flake[0] += random.uniform(-0.4, 0.4)     

            if flake[1] > self.height:
                flake[0] = random.randint(0, self.width)
                flake[1] = -10

    def draw(self, window):
        darkness = self.get_darkness()

       
        if darkness > 0.05:
            self.overlay.fill((10, 10, 30))           
            self.overlay.set_alpha(int(darkness * 160))
            window.blit(self.overlay, (0, 0))

        
        for flake in self.snow:
            
            brightness = int(180 + 75 * darkness)
            color = (brightness, brightness, 255)
            pos   = (int(flake[0]), int(flake[1]))
            pygame.draw.circle(window, color, pos, flake[3])