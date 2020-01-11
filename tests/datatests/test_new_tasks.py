#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import importlib.util
import unittest
import inspect

from parlai.core.agents import Teacher
from parlai.scripts.verify_data import verify, setup_args
import parlai.utils.testing as testing_utils

KEYS = ['missing_text_and_image', 'missing_labels', 'empty_string_label_candidates']


class TestNewTasks(unittest.TestCase):
    """
    Make sure any changes to tasks pass verify_data test.
    """

    def test_verify_data(self):
        parser = setup_args()
        opt = parser.parse_args([], print_args=False)
        changed_task_files = [
            fn
            for fn in testing_utils.git_changed_files()
            if testing_utils.is_new_task_filename(fn)
        ]
        if not changed_task_files:
            return

        found_errors = []
        for file in changed_task_files:
            task = file.split('/')[-2]
            module_name = "%s.tasks.%s.agents" % ('parlai', task)
            task_module = importlib.import_module(module_name)
            subtasks = []
            for x in dir(task_module):
                c = getattr(task_module, x)
                if (
                    inspect.isclass(c)
                    and not inspect.isabstract(c)
                    and issubclass(c, Teacher)
                    and 'BadExampleTeacher' not in x
                    and not x.startswith('_')
                    and x
                    not in [
                        'Teacher',
                        'MultiTaskTeacher',
                        'FixedDialogTeacher',
                        'DialogTeacher',
                    ]
                ):
                    subtasks.append(f'{task}:{x}')

            for subt in subtasks:
                parser = setup_args()
                opt = parser.parse_args(args=['--task', subt], print_args=False)
                opt['task'] = subt
                with self.subTest('--task {}'.format(subt)):
                    with testing_utils.capture_output():
                        text, log = verify(opt, print_parser=False)
                        for key in KEYS:
                            if log[key] != 0:
                                found_errors.append(
                                    'There are {} {} in {}.'.format(log[key], key, subt)
                                )

        if found_errors:
            self.fail("Errors were found.\n{}".format("\n".join(found_errors)))


if __name__ == '__main__':
    unittest.main()
