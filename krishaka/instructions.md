# Here is the summary of work

## Creating package 'krishaka' , dependencies of the package are 
- roscpp
- rospy
- std_msgs
- turtlesim
- gazebo_ros
- gazebo_msgs


## We can create the package with the command 
```bash
catkin_create_pkg krishaka roscpp rospy std_msgs #include other dependencies

```

## After creating a package we run cmd in our workspace folder, which will be buliding the package
```bash
catkin_make
```

## Now our package is ready to work on, Now we need to create an urdf file. URDF(Unified robot description file) consists the information about the geometry of the robots, its joints and physical aspects like mass, friction , area moment of inertia,etc. You can see that file in nano editor by following command

```bash
nano krishaka/urdf/new_mpav.urdf.xacro # The path is absolute path from /home directory
```
### I have some other urdf files in the same folder those are some test urdfs or some sample urdfs.

## Here extension .xacro is there to include different configuration files and also to avoid the repeatation of the code eg.All the four wheels will ne same except there joints and position hence we make use of xacro.  Also we need sensors on robot hence we include other *.urdf.xacro files into the main urdf file.


## The follwing files are sensor files 
<br>
new_depth_camera.gazebo.xacro
new_hokuyo_laser_sensor.gazebo.xacro
new_imu_sensor.gazebo.xacro
</br>

## Now we need to add the necessary plugins into the urdf file for the sensors, we include following plugins
```xml
<plugin name="gazebo_ros_control" filename="libgazebo_ros_control.so">  
<plugin name="differential_drive_controller" filename="libgazebo_ros_diff_drive.so"><!-- for diff drive purpose-->
<plugin name="gazebo_ros_pose" filename="libgazebo_ros_pose.so"> <!--for topic '/pose'-->
```

## Now our urdf file is ready , we check it into rviz, see its configuration and do some changes if needed. For that we have created file 'rviz2.launch' which launches the robot in rviz environment-
<br>
/krishaka/launch/rviz2.launch
</br>

## You can run that file as- 
```bash
roslaunch krishaka rviz2.launch
```

## We can add the sensor info and see it in rviz gui
## Now our urdf is ready to be launched in gazebo environment. We create a launch file named 'world.launch' in /launch directory.
<br>
/krishaka/launch/gazebo.launch
</br>

## You can launch using cmd-
```bash
roslaunch krishaka gazebo.launch
``` 

## Check for the available topics and std_msgs from all topics by follwing cmds-
```bash
rostopic list 
rostopic info 'topic_name'
rosmsg info 'msg_type'
```
##  Also you can see the sensor data in rviz by launching the rviz file as mentioned above.

## Now we need to create a world file to simulate the farm. I got a stl file of a plant online , I reedited that file in bleder, made a crop row out of it and exporeted it as stl file again.
<br>
 /krishaka/folder_for_models/one_crop_row.stl
 </br>

## Now we run gazebo to edit our model(stl file). In gazebo go to 'model editor' include the path of the stl file and edit its physical aspects as per needed by right_clicking on the model.

## Now save the model and exit, now you can make use of that to customize the world. Create world out of that. Save the world file -
<br>
/krishaka/config/new_farm_world.world
</br>

## Now we create a launch file to launch the robot and world simulataneously in gazebo -
<br>
/krishaka/launch/world.launch
</br>

## Launch it by-
```bash
roslaunch krishaka world.launch
```

## Now I have written some scripts in /scripts directory that subscribes to specific topics and publishes on certain topic or simply prints the sensor data.

## To move the robot there is a simple script launch it by-
```bash
rosrun krishaka first_node.py
```
 
