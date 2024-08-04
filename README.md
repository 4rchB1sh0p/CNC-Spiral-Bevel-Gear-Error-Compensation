# CNC Spiral Bevel Gear Error Compensation

## Project Description
This project studies the method of laser vector measurement, error detection principle of spiral bevel gears, and compensates the volumetric error of CNC spiral bevel gear grinding machines.

## Table of Contents
1. [Introduction](#introduction)
2. [Methods of Detecting Error](#methods-of-detecting-error)
   - [Brief Introduction](#brief-introduction)
   - [Conventional Body Diagonal Method](#conventional-body-diagonal-method)
   - [Laser Vector Measurement Method](#laser-vector-measurement-method)
3. [Conclusion](#conclusion)
4. [Future Work](#future-work)
5. [References](#references)
6. [Code Examples](#code-examples)

## Introduction
Spiral bevel gears are crucial parts in the mechanical transmission area. The theory of designing and cutting gear teeth is very complicated. The last working procedure of processing spiral bevel gears is grinding in the computer numerical control (CNC) spiral bevel gear grinding machine. The volumetric error of the grinding machine decides the machining precision to a certain extent. Machining precision of CNC spiral bevel gear grinding machine can be improved through testing and compensating the volumetric error. That's what we will do.

## Methods of Detecting Error

### Brief Introduction
There are two methods of detecting volumetric error, such as individual error detecting and composite error detecting. The former means detecting every error element with laser measuring apparatus and electronic collimation apparatus, the latter is based on a movement model to calculate all error elements with a flexible ball instrument and geometric laser, and so on. The International Organization for Standardization (ISO) suggests that we detect the body diagonal error of the working volume of CNC machine tools to test and compensate the volumetric error quickly because it includes all errors in parallel and vertical directions of the axis.

### Conventional Body Diagonal Method
In order to evaluate the volumetric performance of the machine tools and test volumetric error rapidly, ASME B5.54 and ISO 230-6 standards propose the detecting method of conventional body diagonal. The travel length of three axes of coordinates of CNC machine tools can construct a rectangular solid, which is the working volume. There are four body diagonals and every body diagonal contains the positive and negative directions, so we need to detect eight routes. If ‘p’ means the positive direction, ‘n’ means the negative direction, they are as follows: ppp/nnn, npp/pnn, npn/pnp, ppn/nnp. In the course of detection, three axes of coordinates move simultaneously, all errors of three axes are included in the body diagonal error, so it is difficult to separate them from it.

### Laser Vector Measurement Method
In contrast to the method of conventional body diagonal, the measuring and moving direction in the method of laser vector measurement can be in different directions. Such as the diagonal a􀄺g (ppp), the measuring route in laser vector measurement is as follows: beginning from the point a, firstly move Dx along the positive X axis at a certain rate and pause for several seconds, secondly move Dy along the positive Y axis at a certain rate and pause for several seconds, lastly move Dz along the positive Z axis at a certain rate and pause for several seconds. Repeat the previous steps until arriving at point g. In the course, every data only includes the errors of one axis, so it is convenient to separate the positioning and linear errors from the volumetric error.

## Conclusion
In this study, we tested the volumetric error of the CNC spiral bevel gear grinding machine with the laser vector measurement method, compensated the volumetric error with the software error compensation method, and detected the errors of the spiral bevel gear before and after compensating the volumetric error. Experiments show that the effective compensating of the volumetric error reduces the machining error and improves the machining precision of the machine tool to a certain extent.

