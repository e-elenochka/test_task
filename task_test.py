from unittest import TestCase, main
import link_task

class FormulaTest(TestCase):
    def test_square(self):
        self.assertEqual(link_task.formula('Square TopRight 1 1 Side 1'), 'Square Perimeter 4.00 Area 1.00')

    def test_rectangle(self):
        self.assertEqual(link_task.formula('Rectangle TopRight 2 2 BottomLeft 1 1'), 'Rectangle Perimeter 4.00 Area 1.00')

    def test_circle(self):
        self.assertEqual(link_task.formula('Circle Center 1 1 Radius 2'), 'Circle Perimeter 12.57 Area 12.57')

    def test_no_coord(self):
        with self.assertRaises(Exception) as a:
            link_task.formula('Square TopRight Side ')
            self.assertEqual('Enter the data correctly')


if __name__ == '__main__':
    main()