#!/usr/bin/env python

import asyncio
import json
import websockets
import math

"""
0: nose
1: left_eye
2: right_eye
3: left_ear
4: right_ear
5: left_shoulder
6: right_shoulder
7: left_elbow
8: right_elbow
9: left_wrist
10: right_wrist
11: left_hip
12: right_hip
13: left_knee
14: right_knee
15: left_ankle
16: right_ankle
"""


def calculate_angle(t_x,f_x,t_y,f_y):
    #idk bruh t_y stands for target y
    in_radians = math.atan2(t_y-f_y, t_x-f_x)
    degrees = math.degrees(in_radians)

    if degrees < 0 :
        degrees = (180 + degrees) + 90
    
    else:
        degrees = degrees - 90
    
    return degrees 



async def handler(websocket):
    while True:
        message = await websocket.recv()
        pose_data = json.loads(message)

        r_shoulder_x = pose_data[6]["x"]
        r_shoulder_y = pose_data[6]["y"]

        r_elbow_x = pose_data[8]["x"]
        r_elbow_y = pose_data[8]["y"]

        r_wrist_x= pose_data[10]["x"]
        r_wrist_y = pose_data[10]["y"]


        servo_one_angle =  calculate_angle(r_elbow_x,r_shoulder_x,r_elbow_y,r_shoulder_y)
        servo_two_angle = calculate_angle(r_wrist_x,r_elbow_x,r_wrist_y,r_elbow_y)



        print(f"servo 1: {servo_one_angle}  servo 2: {servo_two_angle}")









async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())