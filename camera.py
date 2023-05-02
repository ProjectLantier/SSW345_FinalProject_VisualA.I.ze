class Camera:
    def __init__(self, resolution: int, focal_length: float):
        self.resolution = resolution
        self.focal_length = focal_length
    
    def take_picture(self) -> str:
        image = f"Picture taken with resolution {self.resolution} and focal length {self.focal_length}"
        return image