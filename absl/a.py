from absl import app
from absl import flags
from absl import logging


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

flags.mark_flags_as_required([
    'input',
])




def main(argv=()):
    del argv
    logging.info('running main.')

    path = FLAGS.input
    file = open(path).readlines()
    for i in range(FLAGS.repeat_times):
        if FLAGS.verbose:
            print(f'{i:3d}: ', end='')
        for line in file:
            print(line, end='')
        print()
    
    logging.set_verbosity(logging.DEBUG)
    logging.log(logging.DEBUG, 'Debug line!!')
    logging.error('Alarming Stuff')

app.run(main)
