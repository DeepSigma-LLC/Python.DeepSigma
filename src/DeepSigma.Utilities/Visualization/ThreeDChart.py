import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import matplotlib.animation as animation
from typing import List, Callable
from src.MetaKit.Objects.ChartObjects.ChartSliderVariable import ChartSliderVariable
from src.MetaKit.Utilities.Username import get_username

class ThreeDChart:
    def __init__(self, x, y, compute_z_callback: Callable, is_surface: bool = True):
        self.animating = [False]
        self.sliders: List[Slider] = []
        self.button_play = None
        self.button_save = None
        self.fig = None
        self.ax = None
        self.x = x
        self.y = y
        self.user_input_parameters: List[float] = []
        self.anim = None
        self.compute_z_callback: Callable = compute_z_callback
        self.slider_variables: List[ChartSliderVariable] = []
        self.is_surface: bool = is_surface

    def add_slider_variable(self, variable: ChartSliderVariable):
        self.slider_variables.append(variable)
        self.user_input_parameters.append(0)

    def __update_plot(self) -> None:
        self.ax.clear()
        self.__build_plot()
        self.__update_chart_format()
        self.fig.canvas.draw_idle()

    def __build_plot(self) -> None:
        z = self.compute_z_callback(self.x, self.y, self.user_input_parameters)
        if self.is_surface:
            self.ax.plot_surface(self.x, self.y, z, cmap='viridis')
        else:
            self.ax.plot(self.x, self.y, z, color='blue')


    def __on_slider_change(self, value: float, triggering_slider) -> None:
        i = self.sliders.index(triggering_slider)
        self.user_input_parameters[i] = value
        self.__update_plot()

    def __animate(self, frame):
        if not self.animating[0]:
            return []

        i = 0
        for slider_variable in self.slider_variables:
            new_value = (self.user_input_parameters[i] + slider_variable.step_size) % slider_variable.maximum_value
            self.user_input_parameters[i] = new_value
            self.sliders[i].set_val(new_value)
            i = i + 1

        self.__update_plot()
        return []

    def __update_chart_format(self) -> None:
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title("Chart Title")

    def __on_button_play_clicked(self, event):
        self.animating[0] = not self.animating[0]
        self.button_play.label.set_text('Pause' if self.animating[0] else 'Play')

    def __on_button_save_clicked(self, event):
        self.animating[0] = not self.animating[0]
        file_path: str = (r'C:\Users\'' & get_username() & r'\Downloads\my_animation.gif')
        self.anim.save(file_path, writer='pillow', fps=20)
        self.animating[0] = not self.animating[0]

    def show_chart(self) -> None:
        plt.style.use("dark_background")
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        self.__build_plot()
        self.__update_chart_format()

        # Sliders
        slider_location_spacing: float = 0.05
        slider_index: int = 0
        starting_slider_location: float = 0.10
        slider_y_location: float = 0
        for slider_variables in self.slider_variables:
            slider_y_location = starting_slider_location + (slider_location_spacing * slider_index)
            ax_slider = plt.axes((0.2, slider_y_location, 0.65, 0.03))
            slider = Slider(ax_slider, label=slider_variables.slider_label, valmin=slider_variables.minimum_value,
                            valmax=slider_variables.maximum_value, valinit=self.user_input_parameters[slider_index],
                            valstep=slider_variables.step_size)
            self.sliders.append(slider)
            self.sliders[slider_index].on_changed(lambda val, s=slider: self.__on_slider_change(val, s))
            slider_index += 1

        # Layout for UI elements
        buffer_spacing: float = 0.1
        plot_bottom_location = slider_y_location + buffer_spacing
        plt.subplots_adjust(bottom = plot_bottom_location, top = 0.9)

        # Play/Pause Button
        ax_button = plt.axes([0.35, 0.03, 0.1, 0.05])
        self.button_play = Button(ax_button, 'Play')
        self.button_play.on_clicked(self.__on_button_play_clicked)

        save_button = plt.axes([0.55, 0.03, 0.1, 0.05])
        self.button_save = Button(save_button, 'Save')
        self.button_save.on_clicked(self.__on_button_save_clicked)

        # Animation
        self.anim = animation.FuncAnimation(self.fig, self.__animate, interval = 20,frames = 100,
                                            cache_frame_data = False, blit = False)
        plt.show()


