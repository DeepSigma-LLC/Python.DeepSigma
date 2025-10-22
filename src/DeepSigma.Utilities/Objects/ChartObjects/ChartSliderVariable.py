

class ChartSliderVariable:
    def __init__(self, maximum, slider_label: str, minimum = 0, step_size = 1):
        self.minimum_value: float = minimum
        self.maximum_value: float = maximum
        self.step_size: float = step_size
        self.slider_control_reference = None
        self.slider_label: str = slider_label