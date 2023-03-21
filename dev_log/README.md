# Dev log
## Note
- Run
```
./Examples/Monocular/mono_general /home/ibois/ORB_SLAM3/Vocabulary/ORBvoc.txt /home/ibois/ORB_SLAM3/Examples/Monocular/orange_camera.yaml /home/ibois/ORB_SLAM3/dataset/ExportedFrames/01
```
- Initial trajectory format:
```
timestamp translation[0, 1, 2] unit_quaternion[x, y, z, w]
```

## TODO
- Check/modify the output trajectory

## Done
- Add `processVideoToKitty.py` to convert a video to the format of KITTY dataset
- In `Examples/Monocular/`, add `mono_general.cc`, which is the modified version of `mono_kitti.cc` to process our own video sequence.
- Change all CMake that using `C++11` to `C++14` to avoid some error.

### Demo
- First time it runs! (It looks laggy because of the framerate of the recording is kinda low)
![](orb_test_0321.gif)