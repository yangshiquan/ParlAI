#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from typing import Dict, Any

task_config: Dict[str, Any] = {}


# task_config['frontend_version'] = 1

"""A short and descriptive title about the kind of task the HIT contains.
On the Amazon Mechanical Turk web site, the HIT title appears in search results,
and everywhere the HIT is mentioned.
"""
task_config['hit_title'] = 'Ask and answer questions about a restaurant'


"""A description includes detailed information about the kind of task the HIT contains.
On the Amazon Mechanical Turk web site, the HIT description appears in the expanded
view of search results, and in the HIT and assignment screens.
"""
task_config['hit_description'] = 'Ask and answer questions about a restaurant.'


"""One or more words or phrases that describe the HIT, separated by commas.
On MTurk website, these words are used in searches to find HITs.
"""
task_config['hit_keywords'] = 'chat,question,answer'


"""A detailed task description that will be shown on the HIT task preview page
and on the left side of the chat page. Supports HTML formatting.
"""
task_config[
    'task_description'
] = '''\'\'\'
In this task, you will need to ask questions about a restaurant, and then provide your own answer to it.<br><br>
Example:<br><br>
------------------- Task Begin ------------------- <br><br>
<b>QA Collector</b>:<br>
meghna address 205_Victoria_Road_Chesterton<br>meghna area west<br>meghna cuisine indian<br>meghna pricerange moderate<br><br>Please provide a question given this context.<br><br>
<b>Worker</b>:<br>
What restaurants are here?<br><br>
<b>QA Collector</b>:<br>
Thanks. And what is the answer to your question?<br><br>
<b>Worker</b>:<br>
There's an indian restaurant named meghna here.<br><br>
------------------- Task Done ------------------- <br><br>
If you are ready, please click "Accept HIT" to start this task.
\'\'\''''
