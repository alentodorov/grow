from . import translation_stats
from babel.messages import catalog
import unittest


class TranslationStatsTestCase(unittest.TestCase):

    def test_tick(self):
        stats = translation_stats.TranslationStats()
        stats.tick(catalog.Message(
            'About',
            'Faoi',
        ), 'ga')
        stats.tick(catalog.Message(
            'Home',
            'Baile',
        ), 'ga')
        stats.tick(catalog.Message(
            'Home',
            'Baile',
        ), 'ga')
        self.assertEqual(
            {
                'messages': {
                    'ga': {
                        'About': 1,
                        'Home': 2,
                    },
                },
                'untranslated': {},
            },
            stats.export())

    def test_tick_none(self):
        stats = translation_stats.TranslationStats()
        stats.tick(None, 'ga')
        self.assertEqual(
            {
                'messages': {},
                'untranslated': {},
            },
            stats.export())

    def test_tick_untranslated(self):
        stats = translation_stats.TranslationStats()
        stats.tick(catalog.Message(
            'About',
            None,
        ), 'ga')
        self.assertEqual(
            {
                'messages': {
                    'ga': {
                        'About': 1,
                    },
                },
                'untranslated': {
                    'ga': {
                        'About': 1,
                    },
                },
            },
            stats.export())


if __name__ == '__main__':
    unittest.main()
