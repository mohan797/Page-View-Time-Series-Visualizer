import unittest
import time_series_visualizer

class DataCleaningTestCase(unittest.TestCase):
    def test_line_plot(self):
        fig = time_series_visualizer.draw_line_plot()
        self.assertIsNotNone(fig, "Line plot figure is None")

    def test_bar_plot(self):
        fig = time_series_visualizer.draw_bar_plot()
        self.assertIsNotNone(fig, "Bar plot figure is None")

    def test_box_plot(self):
        fig = time_series_visualizer.draw_box_plot()
        self.assertIsNotNone(fig, "Box plot figure is None")

if _name_ == "_main_":
    unittest.main()
