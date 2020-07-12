from absl import flags
from absl.testing import absltest
# from absl.testing import parameterized


FLAGS = flags.FLAGS

flags.DEFINE_string(
    'input', None,
    'input file to be printed.')
flags.DEFINE_bool(
    'verbose', False,
    'Whether print verbose information.')
flags.DEFINE_integer(
    'repeat_times', 1,
    'Number of times to repeat.')



class UnitTests(absltest.TestCase):
    def test_usage(self):
        FLAGS.verbose = True
        self.assertTrue(FLAGS.verbose)
        FLAGS.repeat_times = 3
        self.assertEqual(3, FLAGS.repeat_times)

    def test_fail(self):
        FLAGS.verbose = True
        self.assertFalse(FLAGS.verbose)

absltest.main()
