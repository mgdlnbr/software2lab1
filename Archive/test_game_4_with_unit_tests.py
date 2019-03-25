import unittest
import game_4_1 as game


class TestCalculations(unittest.TestCase):


    def setUp(self):
        game.set_globals()
        game.set_input(80, 2, 200)
        game.set_input_nCrop(5000)
        game.set_input_land(400,5000)
        game.set_input_price(20)

        self.end_game = game.end_of_game()
        self.calc_crop = game.calculate_crop()
        self.calc_land = game.calculate_land()
        self.check_land = game.check_land_is_cultivated()


    def test_end_of_game(self):
        result = self.end_game
        self.assertEqual(result,None)

    def test_calc_crop(self):
        result = game.calculate_crop()
        self.assertEqual(5000, result)

    def test_check_land(self):
        result = self.check_land
        self.assertAlmostEqual(802,result)

    def calc_land(self):
        result = self.calc_land()
        result = self.calc_land(402,result)

if __name__ == '__main__':
    unittest.main()
