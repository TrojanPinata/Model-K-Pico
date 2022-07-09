// Copyright 2022 Trojan_Pinata (@Trojan_Pinata)
// SPDX-License-Identifier: GPL-2.0-or-later

#pragma once
//                          0   1   2   3   4
#define MATRIX_ROW_PINS 
    //{ GPIO20, GPIO21, GPIO22, GPIO26, GPIO27, GPIO28 }
    { 26, 27, 29, 31, 32, 34 }
//                          0   1   2   3   4   5   6   7   8    9  10  11   12   13   14   15
#define MATRIX_COL_PINS 
    //{ GPIO2, GPIO3, GPIO4, GPIO5, GPIO6, GPIO7, GPIO8, GPIO9, GPIO10, GPIO11, GPIO12, GPIO13, GPIO14, GPIO15, GPIO16 }
    { 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21 }
#ifdef ENCODER_ENABLE
#define ENCODERS_PAD_A 
    //{ GPIO19 }
    { 25 }
#define ENCODERS_PAD_B 
    //{ GPIO17 }
    { 22 }
#define ENCODER_RESOLUTION 4
#endif


#ifdef OLED_ENABLE
#define OLED_DISPLAY_128X32
#define I2C1_SCL_PIN 1
#define I2C1_SDA_PIN 2
#define OLED_BRIGHTNESS 128
#endif

#define UNUSED_PINS 24
/*
 * Feature disable options
 *  These options are also useful to firmware size reduction.
 */

/* disable debug print */
//#define NO_DEBUG

/* disable print */
//#define NO_PRINT

/* disable action features */
//#define NO_ACTION_LAYER
//#define NO_ACTION_TAPPING
//#define NO_ACTION_ONESHOT
