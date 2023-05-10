from trac_ik_python.trac_ik import IK
import rospy


baselink = rospy.get_param("blue_hardware/baselink")
endlink = rospy.get_param("blue_hardware/endlink")

b1_ik = IK(baselink,endlink)

print(b1_ik.number_of_joints)
print(b1_ik.joint_names)


q = [0,0,0,0,0,0,0]
# - Translation: [-0.023, -0.012, 1.019]
# - Rotation: in Quaternion [0.707, -0.000, 0.707, -0.000]
sol = b1_ik.get_ik(q,-0.023, -0.012, 1.019, 0.707, -0.000, 0.707, -0.000)
print(sol)