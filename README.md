# 随机漫步程序

## 简介

本程序利用Python来生成随机漫步数据，然后利用matplotlib呈现出来。随机漫步指每一次行走都是完全随机的，没有明确的方向，结果是由一系列随机决策决定的。类似于漂浮在水滴上的花粉受到水分子不断的挤压和吸引而在水面上随机移动。所以这个代码可以模拟现实世界的许多情景。

## 创建RandomWalk()类

首先创建一个类，名为RandomWalk，表示随机地选择前进方向。RandomWalk()类包括了三个属性，其中一个是存储随机漫步数的变量，其他两个是两个列表，分别存储经过的每个点的x和y坐标。

```python
from random import choice

class RandomWalk():
	
	def __init__(self,num_points=5000):
		self.num_points=num_points
		self.x_values=[0]
		self.y_values=[0]
		
	def fill_walk(self):
		while len(self.x_values)<self.num_points:
			
			x_direction=choice([1,-1])
			x_distance=choice([0,1,2,3,4,9])
			x_step=x_direction*x_distance
			y_direction=choice([1,-1])
			y_distance=choice([0,1,2,3,4,9])
			y_step=y_direction*y_distance
			
			if x_step==0 and y_step==0:
				continue
			
			next_x=self.x_values[-1]+x_step
			next_y=self.y_values[-1]+y_step
			
			self.x_values.append(next_x)
			self.y_values.append(next_y)
```
这部分程序主要决定随机漫步的移动问题，其中包含多个子部分：

1. 不断漫步，直到列表达到指定长度
```python
while len(self.x_values)<self.num_points:
```
2. 决定前进方向以及沿这个方向前进的距离
```python
x_direction=choice([1,-1])
			x_distance=choice([0,1,2,3,4,9])
			x_step=x_direction*x_distance
			y_direction=choice([1,-1])
			y_distance=choice([0,1,2,3,4,9])
			y_step=y_direction*y_distance
```
3. 为避免重复，用if语句拒绝原地踏步
```python
if x_step==0 and y_step==0:
				continue
```
4. 随机移动后接着计算下一个点的坐标
```python
next_x=self.x_values[-1]+x_step
			next_y=self.y_values[-1]+y_step
```
## 绘制随机漫步图

在关键的绘图部分，首先导入了画图模块pyplot和RandomWalk类，然后创建一个实例，将其储存到rw中，通过调用上一节的函数方法，进行程序的运行。

```python
import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
	rw=RandomWalk(70000)
	rw.fill_walk()
	
	plt.figure(figsize=(10,6))
	point_numbers=list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,
	cmap=plt.cm.Oranges,edgecolor='none',s=1)
	plt.show()
	
	keep_running=input("再来一次?(y/n):")
	if keep_running=='n':
		break
```
这部分代码同样由多部分组成：

1. 只要程序处于活动状态，就不停止
```python
while True:
....
keep_running=input("再来一次?(y/n):")
	if keep_running=='n':
		break
```
2. 给点着色增加美感
```python
point_numbers=list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,c=point_numbers,
	cmap=plt.cm.Oranges,edgecolor='none',s=1)
```
3. 设置绘图窗口的尺寸
```python
plt.figure(figsize=(10,6))
```
## 运行结果

使用编辑器来运行程序：

![第一次运行]([Figure_1.png](https://github.com/lahuan3369/MyPictures/blob/master/Figure_1.png))
![第二次运行](https://github.com/lahuan3369/MyPictures/blob/master/Figure_2.png)
![选择是否继续](https://github.com/lahuan3369/MyPictures/blob/master/README.md)