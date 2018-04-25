#!/bin/python3

def kiir():
  print("bence")

def DrawMiddleTriangle(n):
	for i in range(n+1):
		print((n-i) * " " + i * "x" + (i-1) * "x")

n = int(input("Kérlek add meg a háromszög oldalainak a hosszát! "))
MiddleTriangle(n)
kiir()
