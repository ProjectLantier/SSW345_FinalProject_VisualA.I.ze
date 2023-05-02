class Camera:
    def __init__(self, image_resolution: int, focal_length_mm: float) -> None:
        self.image_resolution = image_resolution
        self.focal_length_mm = focal_length_mm
    
    def take_picture(self) -> str:
        # Add error checking here if needed
        image = f"Picture taken with resolution {self.image_resolution} and focal length {self.focal_length_mm} mm."
        return image
