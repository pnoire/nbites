# Constants.py
# This file holds all Constants which span multiple files

# ****************
# *              *
# * SWITCH BOARD *
# *              *
# ****************

LOG_LOC = True

# *******************
# *                 *
# * MODULE SWITCHES *
# *                 *
# *******************

USE_VISION = True # Disable for faster processing

# *******************
# *                 *
# *   COM HEADER    *
# *                 *
# *******************

PACKET_HEADER = "ilikeyoulots"
NUM_PACKET_ELEMENTS = 20

# ***********************
# *                     *
# * WALK TIME CONSTANTS *
# *                     *
# ***********************

TIME_STEP = 40
TIME_PER_STEP = TIME_STEP/1000.

# ***********************
# *                     *
# *      TEAM STUFF     *
# *                     *
# ***********************

NUM_PLAYERS_PER_TEAM = 4
LENGTH_OF_HALF = 600 #in seconds

# Setup colors
NUM_GAME_TEAM_COLORS = 2
teamColorDict = dict(zip(range(NUM_GAME_TEAM_COLORS),\
                      ("TEAM_BLUE","TEAM_RED")))
(TEAM_BLUE,TEAM_RED) = range(NUM_GAME_TEAM_COLORS)

# *********************************
# *                               *
# * VISION CONNECTION CONSTANTS   *
# *                               *
# *********************************

IMAGE_SIZE = "QVGA"             # 320x240 is what gets processed by vision
CAMERA_FPS = 15
# image constants, used for angle x,y setters
if IMAGE_SIZE == "VGA":
    IMAGE_WIDTH = 640
    IMAGE_HEIGHT = 480
else:
    IMAGE_WIDTH = 320
    IMAGE_HEIGHT = 240

IMAGE_CENTER_X = IMAGE_WIDTH / 2.0
FOV_X_DEG = 46.4
FOV_Y_DEG = 34.8
IMAGE_ANGLE_X = IMAGE_WIDTH / FOV_X_DEG
IMAGE_ANGLE_Y = IMAGE_HEIGHT / FOV_Y_DEG

NUM_TOTAL_BALL_VALUES = 42
NUM_VISION_BALL_VALUES = 9 #unused? 1/20/10
NUM_VISION_FIELD_OBJECT_VALUES = 9

# confidence system for landmark values
NUM_FIELD_OBJECT_CERTAINTIES = 3
(NOTSURE,
 MILDLYSURE,
 SURE) = range(NUM_FIELD_OBJECT_CERTAINTIES)

# confidence system for distances to landmark values
NUM_FIELD_OBJECT_DIST_CERTAINTIES = 4
(BOTH_UNSURE,
 WIDTH_UNSURE,
 HEIGHT_UNSURE,
 BOTH_SURE) = range(NUM_FIELD_OBJECT_DIST_CERTAINTIES)

# *********************************
# *                               *
# *    LOCALIZATION CONSTANTS     *
# *                               *
# *********************************

# Switch to tell us if we are using the lab field or not
USING_LAB_FIELD = False

#---Landmark Constants------#
# Notes:
# FIELD GREEN -- this relates to measurements along the outer edge of the field
# (ie , out of bounds, the very outside green part)
# FIELD WHITE -- this relates to the 'infield' or 'inbounds'

if USING_LAB_FIELD:
    FIELD_WHITE_WIDTH = 500.
    FIELD_WHITE_HEIGHT = 330.
    GREEN_PAD_X = 20.
    GREEN_PAD_Y = 15.
else:
    FIELD_WHITE_WIDTH = 600.0
    FIELD_WHITE_HEIGHT = 400.0
    GREEN_PAD_X = 67.0
    GREEN_PAD_Y = 70.0

FIELD_GREEN_WIDTH = FIELD_WHITE_WIDTH + GREEN_PAD_X * 2.0
FIELD_GREEN_HEIGHT = FIELD_WHITE_HEIGHT + GREEN_PAD_Y * 2.0

FIELD_WIDTH = FIELD_GREEN_WIDTH
FIELD_HEIGHT = FIELD_GREEN_HEIGHT

CENTER_FIELD_X = FIELD_GREEN_WIDTH / 2.0
CENTER_FIELD_Y = FIELD_GREEN_HEIGHT / 2.0

FIELD_GREEN_LEFT_SIDELINE_X = 0
FIELD_GREEN_RIGHT_SIDELINE_X = FIELD_GREEN_WIDTH
FIELD_GREEN_BOTTOM_SIDELINE_Y = 0
FIELD_GREEN_TOP_SIDELINE_Y = FIELD_GREEN_HEIGHT

FIELD_WHITE_BOTTOM_SIDELINE_Y = GREEN_PAD_Y
FIELD_WHITE_TOP_SIDELINE_Y = FIELD_WHITE_HEIGHT + GREEN_PAD_Y
FIELD_WHITE_LEFT_SIDELINE_X = GREEN_PAD_X
FIELD_WHITE_RIGHT_SIDELINE_X = FIELD_WHITE_WIDTH + GREEN_PAD_X

OPP_GOAL_HEADING = 0.
MY_GOAL_HEADING = 180.

# GOAL CONSTANTS
GOAL_POST_CM_HEIGHT = 80.0
GOAL_POST_CM_WIDTH = 10.0
CROSSBAR_CM_WIDTH = 140.0
CROSSBAR_CM_HEIGHT = 5.0
GOAL_POST_RADIUS = GOAL_POST_CM_WIDTH / 2.0

# my left post is left of goalie defending my goal facing the opponent
LANDMARK_MY_GOAL_LEFT_POST_X = FIELD_WHITE_LEFT_SIDELINE_X + GOAL_POST_RADIUS
LANDMARK_MY_GOAL_RIGHT_POST_X = FIELD_WHITE_LEFT_SIDELINE_X + GOAL_POST_RADIUS
LANDMARK_OPP_GOAL_LEFT_POST_X = FIELD_WHITE_RIGHT_SIDELINE_X - GOAL_POST_RADIUS
LANDMARK_OPP_GOAL_RIGHT_POST_X = FIELD_WHITE_RIGHT_SIDELINE_X - GOAL_POST_RADIUS

# measure to the center of the posts, 5 cm off the line
LANDMARK_MY_GOAL_LEFT_POST_Y = CENTER_FIELD_Y + CROSSBAR_CM_WIDTH / 2.0
LANDMARK_MY_GOAL_RIGHT_POST_Y = CENTER_FIELD_Y - CROSSBAR_CM_WIDTH / 2.0
LANDMARK_OPP_GOAL_RIGHT_POST_Y = CENTER_FIELD_Y - CROSSBAR_CM_WIDTH / 2.0
LANDMARK_OPP_GOAL_LEFT_POST_Y = CENTER_FIELD_Y + CROSSBAR_CM_WIDTH / 2.0

GOAL_WIDTH = LANDMARK_MY_GOAL_LEFT_POST_Y - \
    LANDMARK_MY_GOAL_RIGHT_POST_Y

CENTER_CIRCLE_RADIUS = 60.0 # not scaled

if USING_LAB_FIELD:
    GOALBOX_DEPTH = 60.0
    GOALBOX_WIDTH = 200.0
else:
    GOALBOX_DEPTH = 60.0
    GOALBOX_WIDTH = 220.0

MIDFIELD_X = CENTER_FIELD_X
MIDFIELD_Y = CENTER_FIELD_Y

# y distance between sidelines and goalbox
OUTSIDE_GOALBOX_Y = MIDFIELD_Y - GOALBOX_WIDTH*0.5

# my goal box constants relative to (0,0) on my team
MY_GOALBOX_LEFT_X = GREEN_PAD_X
MY_GOALBOX_RIGHT_X = GREEN_PAD_X + GOALBOX_DEPTH
MY_GOALBOX_BOTTOM_Y = MIDFIELD_Y - GOALBOX_WIDTH / 2.
MY_GOALBOX_TOP_Y = MIDFIELD_Y + GOALBOX_WIDTH / 2.
MY_GOALBOX_MIDDLE_Y = (MY_GOALBOX_BOTTOM_Y + MY_GOALBOX_TOP_Y) / 2.

# opp goal box constants relative to (0,0) on my team
OPP_GOALBOX_LEFT_X = FIELD_WHITE_RIGHT_SIDELINE_X - GOALBOX_DEPTH
OPP_GOALBOX_RIGHT_X = FIELD_WHITE_RIGHT_SIDELINE_X
OPP_GOALBOX_BOTTOM_Y = MIDFIELD_Y - GOALBOX_WIDTH / 2.
OPP_GOALBOX_TOP_Y = MIDFIELD_Y + GOALBOX_WIDTH / 2.
OPP_GOALBOX_MIDDLE_Y = (OPP_GOALBOX_BOTTOM_Y + OPP_GOALBOX_TOP_Y) / 2.
OPP_GOAL_MIDPOINT = (OPP_GOALBOX_RIGHT_X, OPP_GOALBOX_MIDDLE_Y)

#LANDMARK TUPLE
NUM_LANDMARKS = 19

(LANDMARK_MY_GOAL_LEFT_POST_ID,
 LANDMARK_MY_GOAL_RIGHT_POST_ID,
 LANDMARK_OPP_GOAL_LEFT_POST_ID,
 LANDMARK_OPP_GOAL_RIGHT_POST_ID,
 LANDMARK_BALL_ID,
 LANDMARK_MY_CORNER_LEFT_L_ID,
 LANDMARK_MY_CORNER_RIGHT_L_ID,
 LANDMARK_MY_GOAL_LEFT_T_ID,
 LANDMARK_MY_GOAL_RIGHT_T_ID,
 LANDMARK_MY_GOAL_LEFT_L_ID,
 LANDMARK_MY_GOAL_RIGHT_L_ID,
 LANDMARK_CENTER_LEFT_T_ID,
 LANDMARK_CENTER_RIGHT_T_ID,
 LANDMARK_OPP_CORNER_LEFT_L_ID,
 LANDMARK_OPP_CORNER_RIGHT_L_ID,
 LANDMARK_OPP_GOAL_LEFT_T_ID,
 LANDMARK_OPP_GOAL_RIGHT_T_ID,
 LANDMARK_OPP_GOAL_LEFT_L_ID,
 LANDMARK_OPP_GOAL_RIGHT_L_ID) = range(NUM_LANDMARKS)

landmarkTuple = (
    "LANDMARK_MY_GOAL_LEFT_POST",
    "LANDMARK_MY_GOAL_RIGHT_POST",
    "LANDMARK_OPP_GOAL_LEFT_POST",
    "LANDMARK_OPP_GOAL_RIGHT_POST",
    "LANDMARK_BALL",
    "LANDMARK_MY_CORNER_LEFT_L",
    "LANDMARK_MY_CORNER_RIGHT_L",
    "LANDMARK_MY_GOAL_LEFT_T",
    "LANDMARK_MY_GOAL_RIGHT_T",
    "LANDMARK_MY_GOAL_LEFT_L",
    "LANDMARK_MY_GOAL_RIGHT_L",
    "LANDMARK_CENTER_LEFT_T",
    "LANDMARK_CENTER_RIGHT_T",
    "LANDMARK_OPP_CORNER_LEFT_L",
    "LANDMARK_OPP_CORNER_RIGHT_L",
    "LANDMARK_OPP_GOAL_LEFT_T",
    "LANDMARK_OPP_GOAL_RIGHT_T",
    "LANDMARK_OPP_GOAL_LEFT_L",
    "LANDMARK_OPP_GOAL_RIGHT_L")

# Landmark Lists for localization
LANDMARK_MY_GOAL_LEFT_POST = [LANDMARK_MY_GOAL_LEFT_POST_X,
                              LANDMARK_MY_GOAL_LEFT_POST_Y,
                              LANDMARK_MY_GOAL_LEFT_POST_ID]
LANDMARK_MY_GOAL_RIGHT_POST = [LANDMARK_MY_GOAL_RIGHT_POST_X,
                               LANDMARK_MY_GOAL_RIGHT_POST_Y,
                               LANDMARK_MY_GOAL_RIGHT_POST_ID]
LANDMARK_OPP_GOAL_LEFT_POST = [LANDMARK_OPP_GOAL_LEFT_POST_X,
                               LANDMARK_OPP_GOAL_LEFT_POST_Y,
                               LANDMARK_OPP_GOAL_LEFT_POST_ID]
LANDMARK_OPP_GOAL_RIGHT_POST = [LANDMARK_OPP_GOAL_RIGHT_POST_X,
                                LANDMARK_OPP_GOAL_RIGHT_POST_Y,
                                LANDMARK_OPP_GOAL_RIGHT_POST_ID]

# Vision IDs for landmarks
NUM_VIS_LANDMARKS = 6
(VISION_YGLP,
 VISION_YGRP,
 VISION_BGLP,
 VISION_BGRP,
 VISION_BG_CROSSBAR,
 VISION_YG_CROSSBAR,
 ) = range(NUM_VIS_LANDMARKS)

visionObjectTuple = ("YGLP",
                     "YGRP",
                     "BGLP",
                     "BGRP")

#Vision IDS for robots
NUM_POSSIBLE_ROBOTS = 6
(RED_1,
RED_2,
RED_3,
BLUE_1,
BLUE_2,
BLUE_3) = range(NUM_POSSIBLE_ROBOTS)

if USING_LAB_FIELD:
    LINE_CROSS_OFFSET = 130
else :
    LINE_CROSS_OFFSET = 180

LANDMARK_OPP_FIELD_CROSS = [FIELD_WHITE_LEFT_SIDELINE_X + LINE_CROSS_OFFSET,
                            MIDFIELD_Y]
LANDMARK_MY_FIELD_CROSS = [FIELD_WHITE_RIGHT_SIDELINE_X - LINE_CROSS_OFFSET,
                           MIDFIELD_Y]


NUM_LOC_SCORES = 3
(BAD_LOC,
 OK_LOC,
 GOOD_LOC) = range(NUM_LOC_SCORES)

GOOD_LOC_XY_UNCERT_THRESH = 30
GOOD_LOC_THETA_UNCERT_THRESH = 20

OK_LOC_XY_UNCERT_THRESH = 130
OK_LOC_THETA_UNCERT_THRESH = 30

BAD_LOC_XY_UNCERT_THRESH = 200
BAD_LOC_THETA_UNCERT_THRESH = 40

##
##--------------------BEHAVIOR CONSTANTS -------------#
##
BALL_TEAMMATE_DIST_GRABBING = 35
BALL_TEAMMATE_BEARING_GRABBING = 85.
BALL_TEAMMATE_DIST_DRIBBLING = 20
