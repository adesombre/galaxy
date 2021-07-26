from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget


class MainWidget(Widget):
	perspective_point_x = NumericProperty(0)
	perspective_point_y = NumericProperty(0)

	def __init__(self, **kwargs):
		super(MainWidget, self).__init__(**kwargs)

	def on_parent(self, widget, parent):
		print("ON PARENT W:" + str(self.width) + " H:" + str(self.height))

	def on_size(self, *args):
		pass
		print("ON SIZE W:" + str(self.width) + " H:" + str(self.height))
		#self.perspective_point_x = self.width / 2
		#self.perspective_point_y = self.height * 0.75

	def on_perpective_point_x(self, widget, value):
		print("PX:" + str(value))

	def on_perpective_point_y(self, widget, value):
		print("PY:" + str(value))


class GalaxyApp(App):
	pass



GalaxyApp().run()


