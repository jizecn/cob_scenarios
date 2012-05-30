import roslib
roslib.load_manifest('cob_generic_states_experimental')
import rospy
import smach
import smach_ros
import time
from simple_script_server import *  # import script
sss = simple_script_server()

class KeepMoving(smach.State):
  def __init__(self):
    smach.State.__init__(self, 
      outcomes=['succeeded'], input_keys=['object_name'])
  print "entering state1"
  def execute(self, ud):
    while 'object_name' not in ud:
      sss.move("sdh", "cylopen")
      sss.move("sdh", "cylclosed")
      #rospy.sleep(0.5)		
    return 'succeeded'
