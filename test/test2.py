import unittest
from tkinter import Tk, Canvas

from Comp_grahaa.main import triangle


class TestTriangleMovement(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.root.title("Test Window")
        self.canvas = Canvas(self.root, width=500, height=500)
        self.canvas.pack()

    def test_movement_left(self):
        self.assertEqual(self.canvas.coords(triangle), [10.0, 10.0, 150.0, 75.0, 20.0, 150.0])
        self.root.event_generate("<Left>")
        self.root.update()
        self.assertEqual(self.canvas.coords(triangle), [7.0, 10.0, 147.0, 75.0, 17.0, 150.0])

    def test_movement_right(self):
        self.assertEqual(self.canvas.coords(triangle), [10.0, 10.0, 150.0, 75.0, 20.0, 150.0])
        self.root.event_generate("<Right>")
        self.root.update()
        self.assertEqual(self.canvas.coords(triangle), [13.0, 10.0, 153.0, 75.0, 23.0, 150.0])

    def test_movement_up(self):
        self.assertEqual(self.canvas.coords(triangle), [10.0, 10.0, 150.0, 75.0, 20.0, 150.0])
        self.root.event_generate("<Up>")
        self.root.update()
        self.assertEqual(self.canvas.coords(triangle), [10.0, 7.0, 150.0, 72.0, 20.0, 147.0])

    def test_movement_down(self):
        self.assertEqual(self.canvas.coords(triangle), [10.0, 10.0, 150.0, 75.0, 20.0, 150.0])
        self.root.event_generate("<Down>")
        self.root.update()
        self.assertEqual(self.canvas.coords(triangle), [10.0, 13.0, 150.0, 78.0, 20.0, 153.0])

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
